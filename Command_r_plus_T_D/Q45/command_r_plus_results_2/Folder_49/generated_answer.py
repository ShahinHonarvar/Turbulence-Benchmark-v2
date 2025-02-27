from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8].lower()
    unique_letters = set(filter(str.isalpha, substring))
    all_permutations = set((''.join(p) for p in permutations(unique_letters, len(unique_letters))))
    palindromes = {p for p in all_permutations if len(p) >= 3 and p == p[::-1]}
    return palindromes