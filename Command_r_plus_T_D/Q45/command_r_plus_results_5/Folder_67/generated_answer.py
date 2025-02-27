from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[2:7] if c.isalpha())).lower()
    arrangements = set((''.join(p) for p in permutations(letters)))
    palindromes = set((a for a in arrangements if len(a) >= 5 and a == a[::-1]))
    return palindromes