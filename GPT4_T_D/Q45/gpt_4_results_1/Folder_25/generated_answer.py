from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    perms = [''.join(p) for p in permutations(s) if len(p) >= 3]
    pals = set((p for p in perms if p == p[::-1]))
    return pals