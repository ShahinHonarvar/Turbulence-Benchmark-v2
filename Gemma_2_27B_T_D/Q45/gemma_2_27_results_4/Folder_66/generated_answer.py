from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[0:6])).lower()
    return set((''.join(p) for p in permutations(letters) if ''.join(p) == ''.join(reversed(''.join(p))) and len(''.join(p)) >= 5))