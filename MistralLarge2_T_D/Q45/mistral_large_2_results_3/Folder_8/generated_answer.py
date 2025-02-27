from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[1:6] if c.isalpha())).lower()
    unique_perms = set((''.join(p) for i in range(5, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in unique_perms if p == p[::-1] and len(p) >= 5}