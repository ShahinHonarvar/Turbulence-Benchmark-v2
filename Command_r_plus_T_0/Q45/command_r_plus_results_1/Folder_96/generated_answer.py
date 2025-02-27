from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((char for char in sub_str if char in english_letters))
    all_permutations = set((''.join(p) for p in permutations(filtered_sub_str)))
    palindromes = set((perm for perm in all_permutations if perm == perm[::-1] and len(perm) >= 6))
    return palindromes