from itertools import permutations as p

def palindromes_between_indices(s):
    pals = set()
    subs = map(list, p(s[2:7], len(s[2:7])))
    subs = [''.join(l) for l in subs if len(l) >= 3]
    for p in subs:
        rev_p = p[::-1]
        if rev_p == p and rev_p.lower() == rev_p and (p.lower() == p):
            pals.add(rev_p)
    return pals