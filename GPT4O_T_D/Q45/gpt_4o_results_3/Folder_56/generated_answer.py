from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[5:10]
    filtered_chars = [char.lower() for char in substring if char.isalpha()]
    possible_palindromes = set()
    if len(filtered_chars) < 5:
        return possible_palindromes
    for length in range(5, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                possible_palindromes.add(perm_str)
    return possible_palindromes