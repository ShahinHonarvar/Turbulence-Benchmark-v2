from itertools import permutations

def palindromes_between_indices(s):
    substr = s[3:10].lower()
    letters = [char for char in substr if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_str = ''.join(perm)
            if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes