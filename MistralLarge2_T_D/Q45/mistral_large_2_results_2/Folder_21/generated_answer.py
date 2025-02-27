import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:9] if c.isalpha()]
    permutations = set((''.join(p) for p in itertools.permutations(letters, 7)))
    palindromes = {p for p in permutations if p.lower() == p.lower()[::-1]}
    return palindromes