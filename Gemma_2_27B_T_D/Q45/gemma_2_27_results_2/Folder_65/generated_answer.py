import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:7] if c.isalpha()]
    return {''.join(p) for p in itertools.permutations(letters) if len(p) >= 5 and ''.join(p).lower() == ''.join(p)[::-1].lower()}