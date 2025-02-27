from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[3:9])).lower()
    unique_palindromes = set()
    for perm in permutations(substring):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 5:
            unique_palindromes.add(perm_str)
    return unique_palindromes