from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:10].lower() if c.isalpha()]
    perms = set((''.join(p) for p in permutations(letters) if len(p) >= 7))
    palindromes = set((p for p in perms if p == p[::-1]))
    return palindromes