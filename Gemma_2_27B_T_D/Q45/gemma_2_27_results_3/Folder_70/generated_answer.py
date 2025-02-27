from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:7] if c.isalpha())).lower()
    return set((p for p in (''.join(perm) for perm in permutations(letters)) if len(p) >= 4 and p == p[::-1]))