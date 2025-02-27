from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[4:7] if c.isalpha()]).lower()
    all_permutations = set((''.join(p) for i in range(len(letters), len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in all_permutations if len(p) >= 4 and p == p[::-1]}