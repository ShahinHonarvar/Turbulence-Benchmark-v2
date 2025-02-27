from itertools import combinations_with_replacement
from string import ascii_lowercase

def palindromes_between_indices(a):
    b = a[5:8]
    return set((a[i:i + len(b)][::-1] for i in range(len(a) - len(b) + 1) if a[i:i + len(b)].lower() == ''.join((c.lower() for c in b))))