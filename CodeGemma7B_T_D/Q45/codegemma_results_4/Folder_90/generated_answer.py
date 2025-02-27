from itertools import permutations

def palindromes_between_indices(text):
    s = text[0:6].lower()
    p = set()
    for i in range(4, len(s) + 1):
        for perm in permutations(s, i):
            p.add(''.join(perm))
    return p