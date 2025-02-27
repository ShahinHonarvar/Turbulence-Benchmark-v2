from functools import reduce

def find_original_set(sets):
    return reduce(lambda s1, s2: s1.union(s2), sets)