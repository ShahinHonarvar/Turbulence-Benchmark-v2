from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    perms = set(permutations(letters))
    palindromes = set((p for p in perms if len(p) >= 5 and p == p[::-1]))
    return palindromes