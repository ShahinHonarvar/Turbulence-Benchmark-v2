from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:4] if c.isalpha())).lower()
    return {''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p)))}