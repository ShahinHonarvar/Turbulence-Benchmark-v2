import re
from itertools import permutations

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:7])
    perms = set((''.join(p) for p in permutations(letters)))
    palindromes = set((p for p in perms if p == p[::-1] and len(p) >= 7))
    return palindromes