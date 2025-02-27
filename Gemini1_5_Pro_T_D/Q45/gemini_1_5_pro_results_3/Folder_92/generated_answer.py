from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((letter for letter in string[4:8] if letter.isalpha())).lower()
    return {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p)))}