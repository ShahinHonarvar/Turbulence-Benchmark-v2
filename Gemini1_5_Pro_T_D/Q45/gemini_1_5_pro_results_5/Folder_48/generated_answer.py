from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[6:9] if char.isalpha())).lower()
    return {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p)))}