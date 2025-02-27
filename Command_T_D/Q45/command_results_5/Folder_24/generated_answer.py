def palindromes_between_indices(s):
    return set((''.join((c for c in s[2:-1] if c.isalpha())).lower() for _ in range(4, 10)))