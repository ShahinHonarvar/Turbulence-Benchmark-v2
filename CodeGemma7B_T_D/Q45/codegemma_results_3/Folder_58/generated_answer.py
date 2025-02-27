from itertools import permutations
import re

def palindromes_between_indices(s):
    f = re.findall('[a-zA-Z]', s[0:7])
    a = set((permutations(f, r) for r in range(6, len(f) + 1)))
    b = (''.join(t) for t in a)
    return {z.upper() for z in b}