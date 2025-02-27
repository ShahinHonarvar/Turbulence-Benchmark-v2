import itertools

def palindromes_between_indices(s):
    return {''.join(p) for p in itertools.product(*[list(d.lower()) for d in s[0:7]]) if p == p[::-1] and all((c in ascii_lowercase for c in ''.join(p)))}