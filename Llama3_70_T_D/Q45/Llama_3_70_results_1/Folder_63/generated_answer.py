from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in permutations(s, r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes