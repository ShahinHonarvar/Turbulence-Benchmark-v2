from functools import reduce
    from itertools import permutations

def palindromes_between_indices(s):
    raw = [char for i, char in enumerate(s) if 3 <= i <= 8 and char.isalpha()]
    return {''.join(p).lower() for p in permutations(raw) if reduce(lambda accum, x: accum + x, p)}