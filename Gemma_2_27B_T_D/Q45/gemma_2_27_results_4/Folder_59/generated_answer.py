from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([c for c in s[8:10] if c.isalpha()])
    return set([''.join(p).lower() for p in permutations(letters) if len(p) >= 3 and ''.join(p).lower() == ''.join(p)[::-1].lower()])