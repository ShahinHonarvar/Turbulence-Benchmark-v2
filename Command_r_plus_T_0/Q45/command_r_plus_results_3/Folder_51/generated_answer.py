from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:6].lower()
    unique_letters = set(filter(str.isalpha, sub_str))
    all_permutations = set((''.join(p) for p in permutations(unique_letters)))
    palindromes = set((p for p in all_permutations if len(p) >= 3 and p == p[::-1]))
    return palindromes