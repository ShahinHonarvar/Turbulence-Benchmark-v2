from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:9])).lower()
    palindromes = set()
    for r in range(7, len(s) + 1):
        for p in permutations(s, r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes