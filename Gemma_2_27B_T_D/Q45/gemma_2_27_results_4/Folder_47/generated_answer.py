from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[3:8] if c.isalpha()]).lower()
    return set([''.join(p) for p in permutations(letters) if len(p) >= 5 and ''.join(p) == ''.join(p)[::-1]])