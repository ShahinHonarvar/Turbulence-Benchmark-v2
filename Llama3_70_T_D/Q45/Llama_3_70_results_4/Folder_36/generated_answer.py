from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:9]
    s = ''.join(filter(str.isalpha, s)).lower()
    pals = {''.join(p) for r in range(3, len(s) + 1) for p in permutations(s) if ''.join(p) == ''.join(p)[::-1]}
    return pals