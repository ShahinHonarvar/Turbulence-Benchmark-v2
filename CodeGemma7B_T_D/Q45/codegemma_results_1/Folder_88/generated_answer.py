from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:8] if c.isalpha()]
    return {''.join(p) for p in permutations(letters, len(letters)) if len(p) >= 6 and p == p[::-1]}