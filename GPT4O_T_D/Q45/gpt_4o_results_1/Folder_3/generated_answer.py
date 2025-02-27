from itertools import permutations

def palindromes_between_indices(s):
    substr = s[7:10].lower()
    perms = set([''.join(p) for i in range(3, len(substr) + 1) for p in permutations(substr, i)])
    return {p for p in perms if p == p[::-1]}