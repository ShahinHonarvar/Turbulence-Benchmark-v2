from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    letters = s[5:9]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    potential_perms = set([''.join(p) for p in permutations(letters, len(letters)) if len(p) > 2])
    palindromes = {perm for perm in potential_perms if perm == perm[::-1]}
    return palindromes