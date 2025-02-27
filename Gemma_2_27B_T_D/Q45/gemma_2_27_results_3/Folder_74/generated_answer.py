from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:7])).lower()
    return set((''.join(p) for p in permutations(letters) if ''.join(p) == ''.join(p)[::-1] and len(''.join(p)) >= 6))