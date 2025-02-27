from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    perms = permutations(letters)
    palindromes = set((p for p in perms if len(p) >= 5 and p == p[::-1]))
    return palindromes