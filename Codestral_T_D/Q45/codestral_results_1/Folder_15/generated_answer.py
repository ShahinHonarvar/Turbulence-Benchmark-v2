from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    characters = s[1:3]
    perms = [''.join(p) for p in permutations(characters)]
    palindromes = {p for p in perms if len(p) >= 3 and p == p[::-1]}
    return palindromes