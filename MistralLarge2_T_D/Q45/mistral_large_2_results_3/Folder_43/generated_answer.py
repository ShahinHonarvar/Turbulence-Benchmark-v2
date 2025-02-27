from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    length = len(letters)
    if length < 4:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(4, length + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes