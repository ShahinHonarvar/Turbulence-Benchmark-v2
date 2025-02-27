from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9]
    substr_english_letters = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for perm in permutations(substr_english_letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromes.add(perm_str)
    return palindromes