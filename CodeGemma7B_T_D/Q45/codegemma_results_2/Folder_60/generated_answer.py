from itertools import permutations

def palindromes_between_indices(text):
    text = text.upper()
    invalid_letters = set('AEIOU')
    letters = [char for char in text[3:7] if char not in invalid_letters]
    return {''.join(p) for p in permutations(letters) if len(p) >= 4}