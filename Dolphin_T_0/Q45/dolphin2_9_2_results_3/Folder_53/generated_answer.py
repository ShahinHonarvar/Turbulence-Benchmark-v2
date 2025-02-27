def palindromes_between_indices(s):
    chars = s[4:9]
    letters = [c for c in chars if c.isalpha()]
    return set((''.join(p) for p in permutations(letters) if len(p) >= 6 and p == p[::-1]))