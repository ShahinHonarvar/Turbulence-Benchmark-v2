from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for i, char in enumerate(string) if 1 <= i <= 9 and char.isalpha())).lower()
    return {''.join(p) for i in range(7, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p)))}