import itertools

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    chars = s[3:6]
    return {''.join(p) for p in itertools.product(set(chars.lower()), repeat=4) if ''.join(p) == ''.join(reversed(p))}