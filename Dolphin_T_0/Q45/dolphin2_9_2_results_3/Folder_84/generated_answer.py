from itertools import permutations, chain
    import re

def palindromes_between_indices(s):
    s = s[4:10]
    st = set(s.lower())
    if len(st) < 3:
        return set()
    palindrom_set = set()
    for p in chain.from_iterable((permutations(st, r) for r in range(len(st), 0, -1))):
        w = ''.join(p)
        if re.fullmatch('^\\\\w+$', w) and len(w) >= 3 and (w == w[::-1]):
            palindrom_set.add(w)
    return palindrom_set