import itertools
import re

def palindromes_between_indices(s):
    s = s[0:7].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations(s, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes