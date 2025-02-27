from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:7].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    palindromes = set((p for p in permutations(filtered_sub_str) if p == p[::-1]))
    palindromes = set((''.join(p) for p in palindromes if len(''.join(p)) >= 4))
    return palindromes