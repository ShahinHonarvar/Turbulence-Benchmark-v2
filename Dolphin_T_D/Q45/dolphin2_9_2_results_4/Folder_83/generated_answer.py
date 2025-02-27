import string
from itertools import permutations as perm

def palindromes_between_indices(s):
    letters = [i.lower() for i in s[2:10] if i in string.ascii_letters]
    perms = [''.join(p) for p in perm(letters, 7)]
    return set((p for p in perms if p == p[::-1]))