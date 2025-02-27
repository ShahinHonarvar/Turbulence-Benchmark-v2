from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:5].lower()
    unique_letters = set(filter(str.isalpha, sub_str))
    all_arrangements = set((''.join(p) for p in permutations(unique_letters)))
    palindromes = set((p for p in all_arrangements if len(p) >= 3 and p == p[::-1]))
    return palindromes