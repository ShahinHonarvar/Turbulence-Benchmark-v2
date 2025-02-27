import itertools

def palindromes_between_indices(s):
    if len(s) <= 6:
        return set(map(str, itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=len(s))))
    else:
        return set(map(str, itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=6)))