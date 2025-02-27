import itertools
import re

def palindromes_between_indices(s):
    s = s[:7].lower()
    s = re.sub('[^a-z]', '', s)
    if len(s) < 7:
        return set()
    letters = sorted(s)
    palindromes = set()
    for p in itertools.permutations(letters):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 7:
            palindromes.add(p)
    return palindromes