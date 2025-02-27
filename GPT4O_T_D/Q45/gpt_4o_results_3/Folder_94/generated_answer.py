from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = s[3:5].lower()
    letters_only = ''.join(filter(str.isalpha, substr))
    if len(letters_only) < 2:
        return set()
    possible_palindromes = set()
    for length in range(3, len(letters_only) + 1):
        for perm in permutations(letters_only, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                possible_palindromes.add(perm_str)
    return possible_palindromes