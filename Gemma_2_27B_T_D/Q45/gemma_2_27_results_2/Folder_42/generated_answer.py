from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[6:10])).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 3 and ''.join(p) == ''.join(p)[::-1]}