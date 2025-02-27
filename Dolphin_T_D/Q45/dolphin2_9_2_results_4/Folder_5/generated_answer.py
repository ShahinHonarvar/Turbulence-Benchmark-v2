def palindromes_between_indices(s):
    chars = [c for c in s[4:9] if c.isalpha()]
    chars = list(map(lambda x: x.lower(), chars))
    return {''.join(chars) for chars in permutations(chars) if chars == chars[::-1]}