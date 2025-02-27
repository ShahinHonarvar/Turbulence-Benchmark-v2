from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:8].lower()
    palindromes = set()
    for l in range(4, len(s) + 1):
        for p in permutations(s, l):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes