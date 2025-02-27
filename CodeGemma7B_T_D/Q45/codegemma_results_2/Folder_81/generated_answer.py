from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((x.lower() for x in text[0:7] if x.isalpha()))
    return {''.join(x) for x in permutations(letters) if len(x) >= 3}