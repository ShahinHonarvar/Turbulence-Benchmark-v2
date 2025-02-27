from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 6 and ''.join(p) == ''.join(p)[::-1]}