import itertools

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[4:9] if c.isalpha())).lower()
    permutations = set((''.join(p) for p in itertools.permutations(letters, 5)))
    palindromes = {p for p in permutations if p == p[::-1]}
    return palindromes