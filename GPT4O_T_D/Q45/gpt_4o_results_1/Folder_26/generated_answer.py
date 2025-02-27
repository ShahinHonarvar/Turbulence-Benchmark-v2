from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[4:7]
    letters = [c.lower() for c in substring if c.isalpha()]
    potential_palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                potential_palindromes.add(perm_str)
    return potential_palindromes