from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    return set((pal for i in range(4, len(s) + 1) for pal in permutations(s, i) if pal == pal[::-1] and len(pal) >= 4))