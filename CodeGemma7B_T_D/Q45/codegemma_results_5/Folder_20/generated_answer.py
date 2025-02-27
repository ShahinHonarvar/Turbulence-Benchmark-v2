from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    return {''.join(p) for p in permutations(text[2:9]) if len(p) >= 4 and p == p[::-1]}