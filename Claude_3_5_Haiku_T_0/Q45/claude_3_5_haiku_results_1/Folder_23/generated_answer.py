from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:7] if char.isalpha()]
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindrome_set.add(perm_str)
    return palindrome_set