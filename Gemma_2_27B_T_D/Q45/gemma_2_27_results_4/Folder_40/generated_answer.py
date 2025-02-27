from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[4:10])).lower()
    return set((''.join(p) for p in permutations(letters) if len(p) >= 7 and ''.join(p) == ''.join(p)[::-1]))