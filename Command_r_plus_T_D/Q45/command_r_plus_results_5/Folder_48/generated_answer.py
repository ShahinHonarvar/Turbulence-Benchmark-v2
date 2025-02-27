from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[6:9].lower()
    letters = set(filter(str.isalpha, sub_str))
    perms = permutations(letters, len(letters))
    palindromes = set((p for p in perms if p == p[::-1] and len(p) >= 4))
    return palindromes