import itertools

def palindromes_between_indices(s):
    substring = s[2:6]
    letters = [c for c in substring if c.isalpha()]
    permutations = set(itertools.permutations(letters, 5))
    palindromes = {''.join(p) for p in permutations if ''.join(p).lower() == ''.join(p).lower()[::-1]}
    return palindromes