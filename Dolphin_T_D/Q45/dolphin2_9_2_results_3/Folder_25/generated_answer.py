from itertools import permutations

def palindromes_between_indices(s):
    pals = set()
    s = s[1:5]
    s = ''.join(sorted(s))
    for p in permutations(s, 3):
        t = ''.join(p)
        t_rev = t[::-1]
        pals.add(t.lower())
        pals.add(t_rev.lower())
    return pals