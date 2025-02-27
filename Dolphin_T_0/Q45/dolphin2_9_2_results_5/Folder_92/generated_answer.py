def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:8]]
    return set((''.join(p) for a in range(7) for b in range(8) if a + b < 8 for p in permutations(letters, a + b) if len(p) >= 4 and ''.join(p) == ''.join(reversed(p))))