from itertools import permutations

def palindromes_between_indices(s):
    return set((word for word in set((''.join(p) for p in permutations(s[7:10].lower(), 4))) if word == word[::-1]))