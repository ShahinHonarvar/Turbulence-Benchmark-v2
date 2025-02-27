from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    letters = [c.lower() for c in letters]
    perms = permutations(letters)
    palindromes = set((p for p in perms if len(p) >= 3 and p == p[::-1]))
    return palindromes