from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7])).lower()
    pals = set((''.join(p) for r in range(6, len(s) + 1) for p in permutations(s) if len(set(p)) > 1 and ''.join(p) == ''.join(p)[::-1]))
    return pals