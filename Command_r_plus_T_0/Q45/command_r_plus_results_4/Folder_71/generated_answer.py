from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:4] if c.isalpha()]
    letters = [c.lower() for c in letters]
    arrangements = set((''.join(p) for p in permutations(letters)))
    palindromes = set((a for a in arrangements if len(a) >= 4 and a == a[::-1]))
    return palindromes