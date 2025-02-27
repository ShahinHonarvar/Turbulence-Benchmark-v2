from itertools import permutations

def palindromes_between_indices(s):
    letters = s.lower()[0:9]
    perms = [''.join(p) for p in permutations(letters) if len(p) > 6 and ''.join(p) == ''.join(p)[::-1]]
    return set(perms)