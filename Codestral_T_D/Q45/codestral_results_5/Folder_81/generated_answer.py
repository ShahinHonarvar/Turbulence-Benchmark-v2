from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:7].lower()
    perms = set((''.join(p) for i in range(3, len(s) + 1) for p in permutations(s, i)))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes