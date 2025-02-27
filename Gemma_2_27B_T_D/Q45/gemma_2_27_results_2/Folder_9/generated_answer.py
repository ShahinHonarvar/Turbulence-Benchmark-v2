from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:7] if c.isalpha())).lower()
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 7 and p == p[::-1]))