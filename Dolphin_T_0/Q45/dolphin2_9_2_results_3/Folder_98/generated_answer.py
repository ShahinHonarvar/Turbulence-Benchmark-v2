def palindromes_between_indices(s):
    s = s[3:6].lower()
    letters = ''.join([c for c in s if c in 'abcdefghijklmnopqrstuvwxyz'])
    return {''.join(p) for p in itertools.permutations(letters) if p == p[::-1] and len(p) >= 4}