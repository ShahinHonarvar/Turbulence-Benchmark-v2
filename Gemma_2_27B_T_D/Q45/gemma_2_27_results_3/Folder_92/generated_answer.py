from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[4:8])).lower()
    return set((''.join(p) for p in permutations(letters) if p == p[::-1] and len(p) >= 4))