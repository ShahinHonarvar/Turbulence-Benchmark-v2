from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:8].lower()
    perms = set(permutations(s))
    palindromes = {''.join(p) for p in perms if p == p[::-1] and len(p) >= 6}
    return palindromes