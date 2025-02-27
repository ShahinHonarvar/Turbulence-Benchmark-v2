def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]
    return {s.upper() for s in set((''.join(p) for p in itertools.permutations(letters, len(letters)))) if s == s[::-1]}