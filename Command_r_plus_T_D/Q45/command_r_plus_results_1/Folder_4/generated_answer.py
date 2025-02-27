import re
    from itertools import permutations

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:10])
    letters = ''.join(letters).lower()
    perms = permutations(letters)
    palindromes = set((p for p in perms if len(p) >= 7 and p == p[::-1]))
    return palindromes