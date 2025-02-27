import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    permutations = set(itertools.permutations(letters, r=3))
    palindromes = {a + b + a for a, b, c in permutations if a.lower() == c.lower()}
    return palindromes