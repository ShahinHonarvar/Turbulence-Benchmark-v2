from itertools import combinations

def palindromes_between_indices(s):
    subs = set(combinations(filter(str.isalpha, s[3:6]), 3))
    pals = set()
    for s in subs:
        p = ''.join(sorted(s)).lower()
        if p == p[::-1]:
            pals.add(p)
    return pals