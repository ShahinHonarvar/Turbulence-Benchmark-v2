from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(perm):
        return perm == perm[::-1]
    substring = s[3:9]
    filtered_chars = [char.lower() for char in substring if char.isalpha()]
    unique_perms = set(permutations(filtered_chars))
    result = set()
    for perm in unique_perms:
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and is_palindrome(perm_str):
            result.add(perm_str)
    return result