from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[2:9])).lower()
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 6 and p == p[::-1]))