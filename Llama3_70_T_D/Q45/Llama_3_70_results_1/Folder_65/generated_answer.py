from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for p in permutations(s, r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes