from itertools import permutations

def palindromes_between_indices(string):
    substring = string[2:6].lower()
    perms = [''.join(p) for p in permutations(substring)]
    palindromes = set((p for p in perms if p == p[::-1] and len(p) >= 3))
    return palindromes