from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join([c for c in s[3:7] if c.isalpha()]).lower()
    all_perms = set((''.join(p) for i in range(3, len(substring) + 1) for p in permutations(substring, i)))
    return {p for p in all_perms if p == p[::-1]}