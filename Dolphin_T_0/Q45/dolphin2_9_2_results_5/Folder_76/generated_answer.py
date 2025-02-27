from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5]
    s = ''.join([c for c in s if c.isalpha()])
    s = s.lower()
    p = set([''.join(p) for p in permutations(s)])
    return set([w for w in p if w == w[::-1] and len(w) >= 4])