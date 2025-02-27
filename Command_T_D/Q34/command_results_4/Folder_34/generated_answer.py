from functools import reduce

def find_original_set(s):
    return reduce(set.intersection, (set(s) for s in range(95)))