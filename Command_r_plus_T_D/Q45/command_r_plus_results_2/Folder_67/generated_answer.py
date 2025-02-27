from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:7].lower()
    letters = [char for char in sub_str if char.isalpha()]
    all_permutations = permutations(letters)
    palindromes = set((perm for perm in all_permutations if len(perm) >= 5 and perm == perm[::-1]))
    return palindromes