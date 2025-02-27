import itertools
import re

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:4]))
    s = s.lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in itertools.permutations(s, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes