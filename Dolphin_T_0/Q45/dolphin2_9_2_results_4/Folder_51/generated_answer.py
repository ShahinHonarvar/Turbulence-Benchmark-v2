from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6]]
    return set((p for p in map(''.join, permutations(letters, 3)) if p == p[::-1]))