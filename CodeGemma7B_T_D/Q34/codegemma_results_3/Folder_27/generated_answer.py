from functools import reduce

def find_original_set(sets):
    return reduce(lambda a, b: a & b, sets)