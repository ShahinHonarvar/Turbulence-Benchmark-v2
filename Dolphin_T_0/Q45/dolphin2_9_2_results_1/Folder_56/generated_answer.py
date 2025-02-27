from itertools import permutations
    from collections import Counter
    from string import ascii_letters

def palindromes_between_indices(s):
    sub_s = s[5:10].lower()
    sub_c = Counter(sub_s)
    extras = [c for c in sub_s if sub_c[c] > 1]
    sub_s = ''.join([c for c in sub_s if c not in extras])
    perms = [''.join(p) for p in permutations(sub_s) if len(p) >= 5]
    palindromes = [p for p in perms if p == p[::-1]]
    return set(palindromes)