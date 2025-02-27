from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[:7])).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 7 and ''.join(p) == ''.join(p)[::-1]}