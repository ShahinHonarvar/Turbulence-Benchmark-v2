from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.isalpha()]
    all_permutations = set((''.join(p) for p in permutations(letters)))
    palindromes = {p for p in all_permutations if len(p) >= 3 and p == p[::-1]}
    return palindromes