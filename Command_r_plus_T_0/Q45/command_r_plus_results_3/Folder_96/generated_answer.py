from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((char for char in sub_str if char in english_letters))
    all_permutations = set((''.join(p) for p in permutations(filtered_sub_str)))
    palindromes = set((p for p in all_permutations if len(p) >= 6 and p == p[::-1]))
    return palindromes