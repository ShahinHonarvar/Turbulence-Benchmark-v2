from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substr = s[1:6].lower()
    letters_only = ''.join(filter(str.isalpha, substr))
    potential_palindromes = set()
    for perm in permutations(letters_only):
        joined_perm = ''.join(perm)
        if joined_perm == joined_perm[::-1] and len(joined_perm) >= 5:
            potential_palindromes.add(joined_perm)
    return potential_palindromes