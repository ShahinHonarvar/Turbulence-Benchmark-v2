from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:4])).lower()
    if len(letters) < 4:
        return set()
    all_permutations = set((''.join(p) for p in permutations(letters, 4)))
    return {p for p in all_permutations if p == p[::-1]}