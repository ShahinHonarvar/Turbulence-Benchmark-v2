from itertools import permutations

def palindromes_between_indices(s):
    letters = s[:7].lower()
    unique_palindromes = set()
    for perm_length in range(7, len(letters) + 1):
        for perm in permutations(letters, perm_length):
            perm_str = ''.join(perm)
            if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
                unique_palindromes.add(perm_str)
    return unique_palindromes