import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    letters = re.findall('[a-z]', s[0:8])
    if len(letters) < 6:
        return set()
    palindromes = set()
    for i in range(6, len(letters) + 1):
        permutations = itertools.product(letters, repeat=i)
        for perm in permutations:
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes