from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[7:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join((ch for ch in sub_str if ch in english_letters))
    all_permutations = set((''.join(p) for p in permutations(sub_str)))
    palindromes = set((p for p in all_permutations if p == p[::-1] and len(p) >= 3))
    return palindromes