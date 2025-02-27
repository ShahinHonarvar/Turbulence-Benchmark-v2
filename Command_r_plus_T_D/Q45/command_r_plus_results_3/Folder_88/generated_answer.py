from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join((ch for ch in sub_str if ch in english_letters))
    perms = set((''.join(p) for p in permutations(sub_str)))
    palindromes = set((p for p in perms if p == p[::-1] and len(p) >= 6))
    return palindromes