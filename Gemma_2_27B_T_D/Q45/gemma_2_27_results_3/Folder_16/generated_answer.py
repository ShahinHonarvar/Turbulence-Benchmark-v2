from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[6:10]))
    return {''.join(p) for p in permutations(letters) if len(p) >= 5 and ''.join(p).lower() == ''.join(p)[::-1].lower()}