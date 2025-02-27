from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha()))
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 3 and p.lower() == p[::-1].lower()))