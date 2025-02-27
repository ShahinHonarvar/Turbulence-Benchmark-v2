from itertools import permutations
from collections import Counter

def palindromes_between_indices(s):
    letters3_8 = s[3:9]
    letters = [c for c in letters3_8 if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    n = len(letters)
    if n < 5:
        return set()
    c = Counter(letters)
    pal = set()
    for p in permutations(c.elements(), n // 2):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 5:
            pal.add(p)
    return pal