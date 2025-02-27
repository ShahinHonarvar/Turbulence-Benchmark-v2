from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 6 and p == p[::-1]))