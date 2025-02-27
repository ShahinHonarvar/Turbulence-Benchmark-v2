from itertools import permutations

def palindromes_between_indices(s):
    letters = s[6:10]
    perms = [''.join(p) for p in permutations(letters)]
    palindromes = {p for p in perms if len(p) >= 4 and p.lower() == p.lower()[::-1]}
    return palindromes