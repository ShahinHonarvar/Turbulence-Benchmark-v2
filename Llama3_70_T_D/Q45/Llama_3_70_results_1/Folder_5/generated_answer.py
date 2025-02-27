from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = ''.join(filter(english_letters.__contains__, s))
    all_permutations = set((''.join(p) for r in range(4, len(s) + 1) for p in permutations(s, r)))
    return set((p for p in all_permutations if p == p[::-1]))