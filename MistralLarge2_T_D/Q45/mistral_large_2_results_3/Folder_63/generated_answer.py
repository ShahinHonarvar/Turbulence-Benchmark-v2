from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[:4] if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters)))
    palindromes = {p for p in perms if is_palindrome(p) and len(p) >= 3}
    return palindromes