from itertools import permutations

def palindromes_between_indices(s):
    substr_set = set()
    search_area = s[0:4].lower()
    letters = ''.join(filter(str.isalpha, search_area))
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                substr_set.add(perm_str)
    return substr_set