from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:5] if c.isalpha()]
    if len(letters) < 5:
        return set()
    letters_lower = ''.join(letters).lower()
    perms = set((''.join(p) for p in permutations(letters_lower, 5)))
    return {p for p in perms if is_palindrome(p)}