from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    palindromes = set()
    for r in range(5, 7):
        for p in permutations(s, r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes