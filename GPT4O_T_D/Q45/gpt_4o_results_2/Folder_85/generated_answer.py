from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    filtered_chars = [ch for ch in substring if ch.isalpha()]
    unique_permutations = set(permutations(filtered_chars, len(filtered_chars)))
    palindromes = set()
    for perm in unique_permutations:
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes