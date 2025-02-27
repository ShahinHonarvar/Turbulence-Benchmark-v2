from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    all_permutations = set((''.join(p) for p in permutations(filtered_sub_str)))
    palindromes = {p for p in all_permutations if p == p[::-1] and len(p) >= 4}
    return palindromes