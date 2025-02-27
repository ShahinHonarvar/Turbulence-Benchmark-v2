from itertools import permutations

def palindromes_between_indices(s: str):
    p = set()
    for a in permutations(s[0:9], len(s[0:9])):
        if ''.join(a).lower() == ''.join(a)[::-1].lower() and len(''.join(a)) >= 7:
            p.add(''.join(a))
    return p