from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    palindromes = set()
    for l in range(6, len(s) + 1):
        for p in permutations(s, l):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes