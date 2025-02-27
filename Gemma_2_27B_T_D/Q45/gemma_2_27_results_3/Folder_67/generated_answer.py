from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[2:7] if c.isalpha()]
    return {''.join(p).lower() for p in permutations(letters) if len(p) >= 5 and ''.join(p).lower() == ''.join(p)[::-1].lower()}