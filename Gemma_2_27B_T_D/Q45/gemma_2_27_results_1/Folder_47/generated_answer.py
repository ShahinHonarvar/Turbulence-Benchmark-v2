from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[3:8]))
    return set((perm for perm in map(''.join, permutations(letters)) if len(perm) >= 5 and perm.lower() == perm.lower()[::-1]))