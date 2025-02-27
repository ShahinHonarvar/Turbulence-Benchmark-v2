from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    s = s[3:6].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 3:
        return set()
    possible_palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            possible_palindromes.add(perm_str)
    return {p for p in possible_palindromes if len(p) >= 3}