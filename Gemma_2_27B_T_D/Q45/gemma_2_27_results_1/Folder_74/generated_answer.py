from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7]))
    return {''.join(perm) for perm in permutations(letters) if ''.join(perm).lower() == ''.join(perm)[::-1].lower() and len(''.join(perm)) >= 6}