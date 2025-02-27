from itertools import permutations

def palindromes_between_indices(s):
    english_letters = ''.join((c for c in s[:5] if c.isalpha()))
    perms = [''.join(p) for p in permutations(english_letters.lower(), len(english_letters))]
    palindromes = set((p for p in perms if p == p[::-1] and len(p) >= 3))
    return palindromes