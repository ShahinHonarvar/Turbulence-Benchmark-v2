import itertools
import re

def palindromes_between_indices(s):
    s = s[2:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for combo in itertools.permutations(s, r):
            p = ''.join(combo)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes