from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:6])).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 4 and ''.join(p) == ''.join(p)[::-1]}