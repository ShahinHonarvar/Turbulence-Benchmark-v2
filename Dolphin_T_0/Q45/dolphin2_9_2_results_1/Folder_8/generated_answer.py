import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.islower()]
    return {''.join(p) for p in itertools.product(letters, repeat=5) if ''.join(p) == ''.join(reversed(''.join(p))) and len(''.join(p)) >= 5}