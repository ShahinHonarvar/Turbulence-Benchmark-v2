from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:6])).lower()
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 3 and p == p[::-1]))