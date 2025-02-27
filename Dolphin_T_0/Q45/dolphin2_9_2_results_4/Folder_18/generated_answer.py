def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join([c for c in s if c.isalpha()])
    return {''.join(p) for p in itertools.permutations(s) if p == p[::-1] and len(p) > 2}