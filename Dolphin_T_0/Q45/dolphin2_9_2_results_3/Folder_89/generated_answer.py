def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    return set(filter(lambda s: len(s) >= 6 and s == s[::-1], (''.join(p) for i in range(len(letters) + 1) for p in itertools.permutations(letters, i))))