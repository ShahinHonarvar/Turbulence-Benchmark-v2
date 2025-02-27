from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([chr(i) for i in range(97, 123) if chr(i) in text[2:8]])
    permutations_set = set([''.join(p) for p in permutations(letters)])
    return {p for p in permutations_set if len(p) >= 6 and p.lower() == p[::-1].lower()}