from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char for char in text[3:9] if char.isalpha()]).lower()
    return {''.join(perm) for perm in permutations(letters) if len(perm) >= 6 and ''.join(perm) == ''.join(reversed(perm))}