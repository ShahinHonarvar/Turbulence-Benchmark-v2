def palindromes_between_indices(s):
    letters = ''.join([c for c in s[2:7] if c.isalpha()])
    return {''.join(p) for p in permutations(letters) if len(p) >= 4 and ''.join(p).lower() == ''.join(p)[::-1].lower()}