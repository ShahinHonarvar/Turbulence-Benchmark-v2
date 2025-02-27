from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    all_arrangements = set((''.join(p) for p in permutations(filtered_sub_str)))
    palindromes = set((arr for arr in all_arrangements if arr == arr[::-1] and len(arr) >= 5))
    return palindromes