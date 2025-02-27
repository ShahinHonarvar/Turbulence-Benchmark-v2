from math import perm
from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[5:10] if c in 'abcdefghijklmnopqrstuvwxyz'])
    n = len(letters)
    palindromes = set()
    for r in range(6, n + 1):
        for p in permutations(letters, r):
            w = ''.join(p)
            if w.lower() == w[::-1].lower() and set(w).issubset(letters):
                palindromes.add(w)
    return palindromes