from itertools import permutations as perm

def palindromes_between_indices(s):
    letters = sorted({char.lower() for char in s[1:7] if char.isalpha()})
    if len(letters) < 3:
        return set()
    return {''.join(p) for p in perm(letters) if p[0] == p[-1]}