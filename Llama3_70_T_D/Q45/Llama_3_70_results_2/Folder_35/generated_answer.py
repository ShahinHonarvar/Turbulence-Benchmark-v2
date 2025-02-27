from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:5].lower()
    perms = set((''.join(p) for p in permutations(s) if len(set(p)) > 1))
    return {p for p in perms if len(p) >= 4 and p == p[::-1]}