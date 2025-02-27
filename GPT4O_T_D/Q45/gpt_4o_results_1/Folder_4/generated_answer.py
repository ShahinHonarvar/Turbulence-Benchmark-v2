from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    filtered_chars = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(filtered_chars):
        joined_perm = ''.join(perm).lower()
        if len(joined_perm) >= 7 and joined_perm == joined_perm[::-1]:
            palindromes.add(joined_perm)
    return palindromes