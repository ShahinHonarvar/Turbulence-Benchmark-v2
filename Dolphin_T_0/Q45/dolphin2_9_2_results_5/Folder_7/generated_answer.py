from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join((c.lower() for c in s.replace(' ', '') if c.isalpha()))
    return set((w for w in map(''.join, permutations(s[1:10])) if len(w) >= 7 and w == w[::-1]))