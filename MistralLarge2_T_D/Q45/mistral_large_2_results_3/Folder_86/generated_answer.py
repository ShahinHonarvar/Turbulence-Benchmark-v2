from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[6:10] if c.isalpha()]).lower()
    perm = set((''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in perm if p == p[::-1] and len(p) >= 4}