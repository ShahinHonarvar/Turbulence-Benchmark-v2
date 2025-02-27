from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9]
    perms = [''.join(p) for i in range(7, len(substring) + 1) for p in permutations(substring, i)]
    palindromes = {w for w in perms if w.lower() == w[::-1].lower() and len(w) >= 7}
    return palindromes