from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in permutations(s, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes