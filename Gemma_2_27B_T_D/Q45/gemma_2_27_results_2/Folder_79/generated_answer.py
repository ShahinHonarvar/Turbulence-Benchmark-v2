from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:8])).lower()
    return set((p for p in map(''.join, permutations(letters)) if p == p[::-1] and len(p) >= 3))