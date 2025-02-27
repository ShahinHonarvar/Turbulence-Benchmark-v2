from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    palindromes = set()
    for r in range(7, len(s) + 1):
        for p in set(permutations(s, r)):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes