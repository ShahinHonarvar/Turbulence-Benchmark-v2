from itertools import permutations as perm

def palindromes_between_indices(s):
    s = s[5:10].lower() if 5 < len(s) and len(s) < 10 else ''
    a = list(perm(s))
    return {(val, val[::-1]) for val in a if len(val) >= 6}