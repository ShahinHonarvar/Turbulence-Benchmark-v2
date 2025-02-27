from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10]))
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 4 and p.lower() == p[::-1].lower()))