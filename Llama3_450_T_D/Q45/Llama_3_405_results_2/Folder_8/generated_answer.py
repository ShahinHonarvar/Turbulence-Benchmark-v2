import itertools
import re

def palindromes_between_indices(s):
    s = s[1:6]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    letters = [c for c in s]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes