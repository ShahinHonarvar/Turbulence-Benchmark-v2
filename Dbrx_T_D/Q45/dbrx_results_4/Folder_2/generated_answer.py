from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:6]]
    perms = [''.join(p) for i in range(1, 7) for p in permutations(chars, i)]
    return {p for p in perms if len(p) >= 6 and p == p[::-1]}