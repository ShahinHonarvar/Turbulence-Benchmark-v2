from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7].lower()
    alpha_chars = ''.join(filter(str.isalpha, substring))
    perms = set([''.join(p) for p in permutations(alpha_chars)])
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 5}
    return palindromes