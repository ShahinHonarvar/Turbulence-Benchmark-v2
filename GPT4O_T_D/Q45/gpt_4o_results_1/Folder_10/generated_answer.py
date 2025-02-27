from itertools import permutations

def palindromes_between_indices(s):
    substr = s[:6]
    cleaned_substr = ''.join(filter(str.isalpha, substr)).lower()
    palindromes = set()
    for perm in permutations(cleaned_substr):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes