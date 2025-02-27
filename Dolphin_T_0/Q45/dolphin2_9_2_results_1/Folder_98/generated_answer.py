import itertools

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[3:6] if c.isalpha())).lower()
    return {''.join(p) for p in itertools.product(letters, repeat=2 * len(letters) // 2) if p == p[::-1]}