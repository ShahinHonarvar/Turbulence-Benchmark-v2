from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = s[1:6].lower()
    letters = [char for char in substring if char.isalpha()]
    perms = set(permutations(letters))
    palindromes = set()
    for p in perms:
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes