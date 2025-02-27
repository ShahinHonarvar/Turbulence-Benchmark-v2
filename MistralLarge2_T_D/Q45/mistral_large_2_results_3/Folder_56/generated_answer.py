import itertools

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[5:10] if c.isalpha()))
    perms = set((''.join(p) for p in itertools.permutations(letters, len(letters))))
    return {p for p in perms if p == p[::-1] and len(p) >= 5}