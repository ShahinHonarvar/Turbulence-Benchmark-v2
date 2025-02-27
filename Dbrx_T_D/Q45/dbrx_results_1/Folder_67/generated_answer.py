from collections import defaultdict

def get_pals_with_len(n, chars):
    pals = set()
    for char in chars:
        pals.add(char * n)
    return pals

def extend_pals(pals, chars):
    extended_pals = set()
    for pal in pals:
        for char in chars:
            extended_pals.add(char + pal + char)
    return extended_pals

def get_all_pals(chars):
    n = len(chars)
    if n < 5:
        return set()
    chars = [char.lower() for char in chars if char.isalpha()]
    chars = ''.join(chars)
    n = min(n, 5)
    pals = get_pals_with_len(1, chars)
    for i in range(2, n + 1):
        pals = extend_pals(pals, chars)
    return pals

def palindromes_between_indices(s):
    return {pal for i in range(2, 7) for j in range(i, 7 + 1) for pal in get_all_pals(s[i:j])}