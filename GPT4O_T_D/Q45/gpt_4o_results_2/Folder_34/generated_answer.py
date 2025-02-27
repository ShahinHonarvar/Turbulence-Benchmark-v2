from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substr = s[5:8].lower()
    substr_letters = [char for char in substr if char.isalpha()]
    if not substr_letters:
        return set()
    potential_palindromes = set()
    for length in range(4, len(substr_letters) + 1):
        for perm in permutations(substr_letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                potential_palindromes.add(perm_str)
    return potential_palindromes