from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:8].lower()
    unique_letters = set(filter(str.isalpha, sub_str))
    palindromes = set()
    for perm in permutations(unique_letters, len(unique_letters)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes