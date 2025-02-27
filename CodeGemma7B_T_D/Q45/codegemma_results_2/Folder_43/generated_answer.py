import itertools

def palindromes_between_indices(s):
    letters = (c.lower() for c in s[2:6] if c.isalpha())
    arrangements = itertools.permutations(letters)
    palindromes = {''.join(p) for p in arrangements if len(p) >= 4}
    return palindromes or set()