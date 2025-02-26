from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:6] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindrome_set = set()
    for perm_length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindrome_set.add(perm_str)
    return palindrome_set