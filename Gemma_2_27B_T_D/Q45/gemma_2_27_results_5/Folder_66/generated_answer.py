from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[:6] if c.isalpha()]).lower()
    return set([''.join(p) for p in permutations(letters) if len(p) >= 5 and ''.join(p) == ''.join(p[::-1])])