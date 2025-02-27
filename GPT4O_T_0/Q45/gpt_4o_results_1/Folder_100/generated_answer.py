from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromes.add(perm_str)
    return palindromes