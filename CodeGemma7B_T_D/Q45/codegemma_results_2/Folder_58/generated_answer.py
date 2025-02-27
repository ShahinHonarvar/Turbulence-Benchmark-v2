from itertools import permutations

def palindromes_between_indices(s):
    return {''.join(i): ''.join(i) for i in permutations(sorted(s[0:7])) if len(''.join(i)) >= 6}