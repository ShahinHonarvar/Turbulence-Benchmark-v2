import itertools

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    clean_substring = ''.join(filter(str.isalpha, substring))
    if len(clean_substring) < 4:
        return set()
    potential_palindromes = set()
    for perm in itertools.permutations(clean_substring):
        perm_str = ''.join(perm)
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            potential_palindromes.add(perm_str)
    return potential_palindromes