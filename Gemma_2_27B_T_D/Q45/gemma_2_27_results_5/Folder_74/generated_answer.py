from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    return {''.join(p) for p in permutations(letters) if ''.join(p).lower() == ''.join(p)[::-1].lower() and len(''.join(p)) >= 6}