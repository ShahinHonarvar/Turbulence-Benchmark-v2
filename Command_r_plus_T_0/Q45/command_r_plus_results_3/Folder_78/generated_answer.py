from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[6:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((char for char in sub_str if char in english_letters))
    all_permutations = set((''.join(p) for p in permutations(filtered_sub_str)))
    palindromes = {p for p in all_permutations if len(p) >= 3 and p == p[::-1]}
    return palindromes