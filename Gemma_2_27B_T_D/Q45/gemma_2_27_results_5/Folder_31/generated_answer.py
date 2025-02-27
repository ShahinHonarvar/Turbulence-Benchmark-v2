from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char for char in text[1:9] if char.isalpha()]).lower()
    return set([''.join(p) for p in permutations(letters) if len(p) >= 6 and ''.join(p) == ''.join(p)[::-1]])