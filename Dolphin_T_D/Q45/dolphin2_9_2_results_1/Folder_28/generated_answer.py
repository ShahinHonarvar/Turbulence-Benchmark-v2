import itertools
    import string

def palindromes_between_indices(s):
    s = s.lower()
    letters = set(s[1:6]).intersection(string.ascii_lowercase)
    return {''.join(p) for c in range(4, 7) for p in itertools.permutations(letters, c) if p == p[::-1] and len(''.join(p)) >= 4}