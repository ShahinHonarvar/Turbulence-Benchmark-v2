from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:5].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    valid_chars = [c for c in substring if c in letters]
    perms = set((''.join(p) for i in range(3, len(valid_chars) + 1) for p in permutations(valid_chars, i)))
    return {p for p in perms if p == p[::-1]}