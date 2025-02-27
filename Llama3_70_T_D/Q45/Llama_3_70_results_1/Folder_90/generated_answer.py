from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    chars = [char for char in s if char.isalpha()]
    perms = [''.join(p) for p in permutations(chars, 4) if len(p) >= 4 and p == p[::-1]]
    return set(perms)