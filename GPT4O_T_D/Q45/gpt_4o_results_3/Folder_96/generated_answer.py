from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    letters = [c for c in substring if c.isalpha()]
    unique_permutations = set(permutations(letters))
    palindromes = set()
    for perm in unique_permutations:
        joined_perm = ''.join(perm)
        if len(joined_perm) >= 6 and joined_perm == joined_perm[::-1]:
            palindromes.add(joined_perm)
    return palindromes