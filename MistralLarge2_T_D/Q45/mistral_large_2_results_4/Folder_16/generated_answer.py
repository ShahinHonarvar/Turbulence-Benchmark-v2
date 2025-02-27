from itertools import permutations

def palindromes_between_indices(string):
    letters = [char for char in string[6:10] if char.isalpha()]
    if len(letters) < 5:
        return set()
    letters = ''.join(letters).lower()
    potential_palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                potential_palindromes.add(perm_str)
    return potential_palindromes