import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    permutations = set((''.join(p) for p in itertools.permutations(letters, 5)))
    palindromes = {p for p in permutations if p == p[::-1]}
    return palindromes