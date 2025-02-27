def palindromes_between_indices(s):
    s = s[3:7].lower()
    return {''.join(p) for r in range(3, len(s) + 1) for p in permutations(s, r) if p == p[::-1]}