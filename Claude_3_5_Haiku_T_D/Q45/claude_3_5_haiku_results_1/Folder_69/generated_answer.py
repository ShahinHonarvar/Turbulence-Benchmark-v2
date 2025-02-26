from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    result = set()
    for perm_length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            perm_str = ''.join(perm)
            if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result