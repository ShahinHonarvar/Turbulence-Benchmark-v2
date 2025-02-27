from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:8])).lower()
    return set((p for p in set((''.join(perm) for perm in permutations(letters))) if len(p) >= 3 and p == p[::-1]))