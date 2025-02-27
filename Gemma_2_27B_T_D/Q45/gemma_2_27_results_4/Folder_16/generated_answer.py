from itertools import permutations

def palindromes_between_indices(s):
    letters = s[6:10].lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 5 and ''.join(p) == ''.join(p)[::-1]}