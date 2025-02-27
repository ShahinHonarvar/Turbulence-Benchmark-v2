from itertools import permutations

def palindromes_between_indices(s):
    english_chars = ''.join(filter(str.isalpha, s[6:10]))
    perms = set()
    for r in range(5, len(english_chars) + 1):
        perms.update((''.join(p) for p in permutations(english_chars.lower(), r)))
    return set((p for p in perms if p == p[::-1]))