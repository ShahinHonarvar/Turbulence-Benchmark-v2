from itertools import product

def palindromes_between_indices(s):
    s = s[6:10].lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in product(s, repeat=r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes