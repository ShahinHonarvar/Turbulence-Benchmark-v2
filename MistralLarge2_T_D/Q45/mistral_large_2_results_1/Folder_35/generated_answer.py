from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    if len(letters) < 4:
        return set()

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes