from itertools import permutations, combinations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    return {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if p == p[::-1]}