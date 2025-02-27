from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    all_permutations = permutations(letters)
    palindromes = set((p for p in all_permutations if len(p) >= 7 and p == p[::-1]))
    return palindromes