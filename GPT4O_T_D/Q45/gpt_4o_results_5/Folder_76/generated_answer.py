from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 5:
        return set()
    sub_str = s[1:5]
    perms = set((''.join(p) for p in permutations(sub_str) if ''.join(p) == ''.join(p)[::-1] and len(''.join(p)) >= 4))
    return perms