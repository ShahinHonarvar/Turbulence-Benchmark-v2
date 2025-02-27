from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[2:10] if c.isalpha())).lower()
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 6 and p == p[::-1]))