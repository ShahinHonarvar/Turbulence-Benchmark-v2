from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10]
    english_letters = ''.join(filter(str.isalpha, s)).lower()
    if len(english_letters) < 6:
        return set()
    perms = set((''.join(p) for p in permutations(english_letters)))
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 6}
    return palindromes