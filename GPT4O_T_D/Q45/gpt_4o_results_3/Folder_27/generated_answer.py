from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    english_letters = ''.join(filter(str.isalpha, substring))
    perms = set((''.join(p) for p in permutations(english_letters) if len(p) >= 6))
    return {p for p in perms if p == p[::-1]}