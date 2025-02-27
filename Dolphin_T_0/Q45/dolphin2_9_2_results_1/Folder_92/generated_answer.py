def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:8] if 'a' <= c.lower() <= 'z']
    return {''.join(p) for p in itertools.permutations(chars, int(len(chars) / 2) * 2) if p == ''.join(reversed(p))}