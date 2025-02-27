from itertools import permutations
import re

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = re.findall('[a-z]', s)
    return {p for r in range(7, len(letters) + 1) for p in set((''.join(p) for p in permutations(letters, r) if p == p[::-1]))}