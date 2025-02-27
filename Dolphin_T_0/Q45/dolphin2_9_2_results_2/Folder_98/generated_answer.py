def palindromes_between_indices(s):
    letters = [c for c in s[2:6].lower() if c.isalpha()]
    if len(letters) < 4:
        return set()
    return set((''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if ''.join(p).lower() == ''.join(p[::-1]).lower()))