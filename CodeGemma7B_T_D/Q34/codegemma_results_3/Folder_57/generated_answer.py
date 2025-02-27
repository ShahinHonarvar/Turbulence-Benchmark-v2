from math import inf

def find_original_set(*args):
    minimum = set(range(inf))
    for s in args:
        minimum &= s
    return minimum