from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:6])).lower()
    return set((p for p in (''.join(perm) for perm in permutations(letters)) if p == p[::-1] and len(p) >= 6))