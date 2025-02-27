from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    s = ''.join(filter(str.isalpha, s))
    perms = [''.join(p) for p in permutations(s) if len(p) >= 5]
    palindromes = set((p for p in perms if p == p[::-1]))
    return palindromes