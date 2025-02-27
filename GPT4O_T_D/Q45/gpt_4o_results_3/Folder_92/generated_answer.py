from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8].lower()
    valid_chars = ''.join(filter(str.isalpha, substring))
    if len(valid_chars) < 4:
        return set()
    palindromes = set()
    for perm in permutations(valid_chars):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes