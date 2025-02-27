from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(str.isalpha, s[1:7])))
    return {''.join(p) for p in permutations(letters) if len(''.join(p)) >= 7 and ''.join(p).lower() == ''.join(p[::-1]).lower()}