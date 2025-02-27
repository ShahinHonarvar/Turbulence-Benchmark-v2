from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[6:9] if c.isalpha())).lower()
    return {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(p)[::-1]}