from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[5:10])).lower()
    palindromes = set()
    for r in range(4, len(substring) + 1):
        for p in permutations(substring, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes