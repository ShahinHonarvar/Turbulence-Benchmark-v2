from itertools import permutations as perm

def palindromes_between_indices(s):
    backdrop = s[3:8 + 1]
    backdrop = ''.join([c.lower() for c in backdrop])
    if backdrop.isalpha():
        return {''.join(p): p for p in perm(backdrop)}
    else:
        return set()