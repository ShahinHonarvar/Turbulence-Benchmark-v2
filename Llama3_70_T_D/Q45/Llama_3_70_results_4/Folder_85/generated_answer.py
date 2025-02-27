from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    perms = [''.join(p) for p in permutations(s) if len(p) >= 7]
    return set((p for p in perms if p == p[::-1]))