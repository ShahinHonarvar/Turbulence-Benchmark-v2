from itertools import permutations

def palindromes_between_indices(s):
    sub_s = ''.join(filter(str.isalpha, s[3:5])).lower()
    if len(sub_s) < 3:
        return set()
    perms = set((''.join(p) for p in permutations(sub_s)))
    palindromes = set((s for s in perms if s == s[::-1] and len(s) >= 3))
    return palindromes