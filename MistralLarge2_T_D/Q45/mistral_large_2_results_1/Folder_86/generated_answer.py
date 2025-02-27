import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    perms = set((''.join(p) for r in range(4, len(letters) + 1) for p in itertools.permutations(letters, r)))
    return {p for p in perms if p == p[::-1]}