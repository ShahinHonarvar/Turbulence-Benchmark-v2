from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    perms = set(permutations(substring, r=None))
    palindromes = {''.join(p) for p in perms if len(p) >= 6 and p == p[::-1]}
    return palindromes