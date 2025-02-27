from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    letters = [char for char in substring if char.isalpha()]
    result = set()
    if len(letters) < 7:
        return result
    for perm in set(permutations(letters, len(letters))):
        perm_str = ''.join(perm)
        for length in range(7, len(perm_str) + 1):
            if perm_str[:length] == perm_str[:length][::-1]:
                result.add(perm_str[:length])
    return result