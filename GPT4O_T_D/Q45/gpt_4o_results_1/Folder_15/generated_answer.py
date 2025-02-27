from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    substr = ''.join(filter(str.isalpha, s[1:3])).lower()
    perms = set([''.join(p) for p in permutations(substr)])
    palindromes = {p for p in perms if len(p) >= 3 and p == p[::-1]}
    return palindromes