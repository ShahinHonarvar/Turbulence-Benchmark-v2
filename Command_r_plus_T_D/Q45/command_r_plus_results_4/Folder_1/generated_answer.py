from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:8].lower()
    unique_letters = set(filter(str.isalpha, sub_str))
    all_permutations = set((''.join(p) for p in permutations(unique_letters)))
    palindromes = set((p for p in all_permutations if len(p) >= 5 and p == p[::-1]))
    return palindromes