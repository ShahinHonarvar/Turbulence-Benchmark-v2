from itertools import permutations

def palindromes_between_indices(string):
    return {''.join(p) for i in range(4, 7) for p in permutations(sorted([char for char in string[1:7] if char.isalpha()])) if p[-i:] == p[:i]}