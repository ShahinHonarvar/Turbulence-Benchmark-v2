from itertools import permutations

def palindromes_between_indices(str):
    str = str.casefold()
    start = 'abc'
    end = 'xyz'
    str_mid = str[2:6]
    mid = str_mid[::int(-1)]
    return {''.join(p) for p in permutations(mid) if start <= p <= end}