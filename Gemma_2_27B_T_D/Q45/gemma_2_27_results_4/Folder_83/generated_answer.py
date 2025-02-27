from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10])).lower()
    return set((p for p in [''.join(perm) for perm in permutations(letters)] if len(p) >= 7 and p == p[::-1]))