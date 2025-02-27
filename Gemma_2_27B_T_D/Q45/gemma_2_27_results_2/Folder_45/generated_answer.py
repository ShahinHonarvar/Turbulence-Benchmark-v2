def palindromes_between_indices(s):
    letters = ''.join((c for c in s[5:10] if c.isalpha())).lower()
    return {p for p in set((''.join(perm) for perm in permutations(letters))) if len(p) >= 4 and p == p[::-1]}