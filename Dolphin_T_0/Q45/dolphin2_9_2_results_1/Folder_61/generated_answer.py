from itertools import permutations

def palindromes_between_indices(s):
    pals = set()
    s = s[:8]
    for p in permutations(s.lower(), len(s)):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 7:
            pals.add(p)
    return pals