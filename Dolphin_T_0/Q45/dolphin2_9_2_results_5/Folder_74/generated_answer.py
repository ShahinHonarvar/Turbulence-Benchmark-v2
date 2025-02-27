from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[1:7] if c.isalpha()]
    if len(chars) < 6 or len(set(chars)) == 1:
        return set()
    res = set()
    for p in permutations(chars, len(chars)):
        if p == p[::-1]:
            res.add(''.join(p).lower())
    return res