import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    permutations = set((''.join(p) for r in range(5, len(letters) + 1) for p in itertools.permutations(letters, r)))
    return {p for p in permutations if p.lower() == p.lower()[::-1]}