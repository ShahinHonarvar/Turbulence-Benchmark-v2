from itertools import permutations

def palindromes_between_indices(string):
    palindromes = {''.join(p) for p in permutations(string[0:4].lower())}
    return {p for p in palindromes if len(p) >= 3 and p == p[::-1]}