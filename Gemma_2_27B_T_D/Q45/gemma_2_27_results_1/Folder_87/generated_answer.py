from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[3:10] if c.isalpha()]
    return {''.join(p) for p in permutations(letters) if len(p) >= 3 and ''.join(p).lower() == ''.join(p)[::-1].lower()}