from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[0:6])).lower()
    return set((perm for perm in {''.join(p) for p in permutations(letters) if len(perm) >= 4} if perm == perm[::-1]))