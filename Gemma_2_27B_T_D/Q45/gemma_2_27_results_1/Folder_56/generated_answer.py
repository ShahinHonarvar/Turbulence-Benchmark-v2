from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[5:10] if c.isalpha())).lower()
    return set((p for p in (p + p[::-1] for p in map(''.join, permutations(letters))) if len(p) >= 5 and p == p[::-1]))