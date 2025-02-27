from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9].lower()
    letters = [char for char in substr if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 3:
            palindromes.add(perm_str)
    return palindromes