from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:9])).lower()
    return set((perm for perm in set((''.join(p) for p in permutations(letters))) if len(perm) >= 7 and perm == perm[::-1]))