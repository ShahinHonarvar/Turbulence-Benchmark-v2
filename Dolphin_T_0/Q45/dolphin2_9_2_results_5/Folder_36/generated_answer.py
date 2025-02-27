def palindromes_between_indices(s):
    s = s[5:9].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return set(filter(lambda p: len(p) >= 3, [''.join(p) for p in itertools.permutations(s) if p == p[::-1] and all((c in alphabet for c in p))]))