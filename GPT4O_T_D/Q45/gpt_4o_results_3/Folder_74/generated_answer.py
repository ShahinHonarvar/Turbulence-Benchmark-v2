from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = ''.join([c for c in s[1:7] if c.isalpha()])
    perms = set((''.join(p) for p in permutations(substring) if len(p) > 5))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes