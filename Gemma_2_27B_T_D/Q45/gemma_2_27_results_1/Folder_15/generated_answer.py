def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:3] if c.isalpha())).lower()
    return {s for s in set((''.join(p) for p in [list(permutations(letters))] if len(s) >= 3 and s == s[::-1]))}