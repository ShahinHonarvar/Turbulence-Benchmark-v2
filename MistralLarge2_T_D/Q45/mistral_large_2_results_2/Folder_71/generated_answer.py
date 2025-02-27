from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[1:4] if c.isalpha()]
    n = len(letters)
    if n < 4:
        return set()
    palindromes = set()
    for length in range(4, n + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
    return palindromes