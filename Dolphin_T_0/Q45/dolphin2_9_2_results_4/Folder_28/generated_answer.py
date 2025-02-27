def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:6] if c.isalpha()))
    return {p for i in range(4, len(letters) + 1) for p in set(letters[i:]) if p == p[::-1]}