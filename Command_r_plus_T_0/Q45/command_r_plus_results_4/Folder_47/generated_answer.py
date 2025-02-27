from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join(filter(lambda x: x in english_letters, sub_str))
    all_permutations = set((''.join(p) for p in permutations(sub_str)))
    palindromes = set((p for p in all_permutations if p == p[::-1] and len(p) >= 5))
    return palindromes