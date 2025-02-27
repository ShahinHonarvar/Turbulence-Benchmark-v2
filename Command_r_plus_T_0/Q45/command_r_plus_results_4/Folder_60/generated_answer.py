from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:7].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_str = ''.join((c for c in sub_str if c in english_letters))
    all_permutations = set((''.join(p) for p in permutations(filtered_str)))
    palindromes = set((p for p in all_permutations if len(p) >= 4 and p == p[::-1]))
    return palindromes