def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[2:5]]))
    return {''.join(p) for p in product(letters, repeat=3) if p == p[::-1] and len(set(p)) < 3}