from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:6]
    out = set()
    for p in permutations(s, 5):
        if p == p[::-1]:
            out.add(''.join(p))
    for p in permutations(s, 6):
        if p == p[::-1]:
            out.add(''.join(p))
    return out