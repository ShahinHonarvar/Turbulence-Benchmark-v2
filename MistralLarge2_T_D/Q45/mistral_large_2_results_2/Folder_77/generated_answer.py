from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7].lower()
    letters = set(substring) - set('0123456789')
    perms = set((''.join(p) for i in range(4, len(substring) + 1) for p in permutations(letters, i)))
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 4}
    return palindromes