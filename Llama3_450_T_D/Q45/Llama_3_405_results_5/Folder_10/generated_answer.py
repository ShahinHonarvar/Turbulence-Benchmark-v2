from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:6])).lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in permutations(s, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes