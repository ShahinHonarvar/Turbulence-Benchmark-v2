from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1].lower()
    letters = [c for c in s[0:8] if c.isalpha()]
    perms = set([''.join(p) for p in permutations(letters, 4)])
    return set((w for w in perms if is_palindrome(w)))