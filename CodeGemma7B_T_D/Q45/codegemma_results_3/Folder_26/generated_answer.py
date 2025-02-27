from itertools import permutations

def palindromes_between_indices(string):
    letters = [char for char in string[4:7].lower()]
    if not letters:
        return set()
    return {''.join(p) for p in permutations(letters) if p == p[::-1]}