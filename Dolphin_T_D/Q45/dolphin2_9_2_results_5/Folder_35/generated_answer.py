def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5]]
    return {''.join(p) for p in itertools.product(letters, repeat=2) if p == p[::-1]}