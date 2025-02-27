from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:6])).lower()
    return set([''.join(p) for p in permutations(letters) if len(p) >= 4 and ''.join(p) == ''.join(p)[::-1]])