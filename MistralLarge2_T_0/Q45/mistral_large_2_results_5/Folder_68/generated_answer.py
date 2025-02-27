import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:9] if c.isalpha()]
    permutations = set((''.join(p) for r in range(4, len(letters) + 1) for p in itertools.permutations(letters, r)))
    palindromes = {p for p in permutations if p.lower() == p.lower()[::-1]}
    return palindromes