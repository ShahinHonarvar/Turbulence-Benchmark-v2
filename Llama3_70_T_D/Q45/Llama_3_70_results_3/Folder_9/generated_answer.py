from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    english_chars = 'abcdefghijklmnopqrstuvwxyz'
    chars_in_range = [char for char in s if char in english_chars]
    return set((''.join(p) for r in range(7, len(chars_in_range) + 1) for p in permutations(chars_in_range, r) if ''.join(p) == ''.join(p)[::-1]))