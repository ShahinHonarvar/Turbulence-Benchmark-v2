from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes