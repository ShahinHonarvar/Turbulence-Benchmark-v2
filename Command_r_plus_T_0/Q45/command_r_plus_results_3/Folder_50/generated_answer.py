from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    all_permutations = permutations(letters)
    palindromes = set((p for p in all_permutations if p == p[::-1] and len(p) >= 5))
    return palindromes