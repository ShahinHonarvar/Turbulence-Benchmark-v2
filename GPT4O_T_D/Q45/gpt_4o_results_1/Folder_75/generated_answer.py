from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = s[2:5].lower()
    letters = [char for char in substr if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes