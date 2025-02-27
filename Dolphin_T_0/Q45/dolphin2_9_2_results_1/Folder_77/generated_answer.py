def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7]]
    return {''.join(p) for p in itertools.permutations(letters) if len(p) >= 4 and p == p[::-1]}