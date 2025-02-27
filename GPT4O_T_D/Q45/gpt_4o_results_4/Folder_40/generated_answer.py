from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[4:10].lower()
    alpha_sub_s = ''.join(filter(str.isalpha, sub_s))
    if len(alpha_sub_s) < 7:
        return set()
    perms = set(permutations(alpha_sub_s, 7))
    palindromes = {p for p in perms if p == p[::-1]}
    return {''.join(p) for p in palindromes}