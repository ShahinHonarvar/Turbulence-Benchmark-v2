from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[5:7].lower()
    unique_letters = set(filter(str.isalpha, sub_str))
    palindromes = set((perm[0] + perm[1] + perm[1] + perm[0] for perm in permutations(unique_letters, 2)))
    return palindromes