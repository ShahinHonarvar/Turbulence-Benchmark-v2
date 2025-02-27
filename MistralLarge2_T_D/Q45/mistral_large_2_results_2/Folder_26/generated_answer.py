import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    perms = set(itertools.permutations(letters, r=3))
    palindromes = {''.join(p) for p in perms if p == p[::-1]}
    return palindromes