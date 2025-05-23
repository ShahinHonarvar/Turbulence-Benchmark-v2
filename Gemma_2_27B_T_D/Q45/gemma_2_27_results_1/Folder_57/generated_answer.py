from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[2:6])).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 5 and ''.join(p) == ''.join(p)[::-1]}