def palindromes_between_indices(s):
    d = [c.lower() for c in s[0:9]] if len(s) > 8 else [c.lower() for c in s]
    return {w for w in set((''.join(p) for p in permutations(d))) if w == w[::-1] and len(w) > 6}