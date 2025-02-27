from itertools import permutations as _permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(lambda x: x.isalnum(), s)[4:10]))
    return set(filter(lambda x: x == x[::-1], map(''.join, _permutations(letters))))