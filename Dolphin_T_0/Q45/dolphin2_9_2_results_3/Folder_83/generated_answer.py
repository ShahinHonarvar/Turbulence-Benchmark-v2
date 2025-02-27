from itertools import permutations
    import re

def palindromes_between_indices(s):
    s = s[2:10]
    s = re.sub('\\\\W+', '', s)
    s = s.lower()
    pals = set()
    for i in range(7, len(s) + 1):
        perm = permutations(s, i)
        for p in list(perm):
            if ''.join(p) == ''.join(reversed(p)):
                pals.add(''.join(p))
    return pals