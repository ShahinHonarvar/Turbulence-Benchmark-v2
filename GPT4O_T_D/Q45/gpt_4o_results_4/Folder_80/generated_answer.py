from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    slice_str = s[3:9].lower()
    filtered_chars = [char for char in slice_str if char.isalpha()]
    if len(filtered_chars) < 7:
        return set()
    palindromes = set()
    for perm in permutations(filtered_chars):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes