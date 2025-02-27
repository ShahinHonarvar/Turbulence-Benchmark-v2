from itertools import permutations

def palindromes_between_indices(str):
    s = ''.join((i for i in str[1:5].lower() if i.isalpha()))
    if len(s) < 3:
        return set()
    words = list((' '.join(p) for p in permutations(s)))
    return {x for x in words if x == x[::-1]}