from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:8].lower()
    letters = [char for char in sub_string if char.isalpha()]
    palindromic_set = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromic_set.add(perm_str)
    return palindromic_set