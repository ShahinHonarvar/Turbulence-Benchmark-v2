import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    permutations = set((''.join(p) for r in range(3, len(letters) + 1) for p in itertools.permutations(letters, r) if p == p[::-1]))
    return permutations