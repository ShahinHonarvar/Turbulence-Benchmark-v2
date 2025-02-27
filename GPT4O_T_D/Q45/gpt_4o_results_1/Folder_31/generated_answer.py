from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    filtered_chars = [c for c in s if c.isalpha()]
    unique_palindromes = set()
    for perm in permutations(filtered_chars, len(filtered_chars)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and perm_str == perm_str[::-1]:
            unique_palindromes.add(perm_str)
    return unique_palindromes