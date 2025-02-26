from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:7] if char.isalpha()]
    palindromes_set = set()
    for length in range(5, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_str = ''.join(perm)
            if len(set(perm_str)) >= 5 and perm_str == perm_str[::-1]:
                palindromes_set.add(perm_str)
    return palindromes_set