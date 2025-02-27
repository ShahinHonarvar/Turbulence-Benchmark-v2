from itertools import permutations

def palindromes_between_indices(s):
    sub = s[4:7].lower()
    sub_set = set(sub)
    sub_perms = [''.join(p) for p in permutations(sub, 3)]
    palindromes = [p for p in sub_perms if p[::-1] in sub_perms]
    pal_set = set(palindromes)
    return pal_set if len(pal_set) > 0 else set()