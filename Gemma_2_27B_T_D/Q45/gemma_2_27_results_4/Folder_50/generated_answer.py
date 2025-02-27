from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[4:9])).lower()
    return set((p for p in map(''.join, permutations(letters)) if len(p) >= 5 and p == p[::-1]))