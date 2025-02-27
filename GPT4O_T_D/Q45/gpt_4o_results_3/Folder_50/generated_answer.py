from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[4:9].lower()
    letters = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    if len(letters) < 5:
        return set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 5:
            palindromes.add(perm_str)
    return palindromes