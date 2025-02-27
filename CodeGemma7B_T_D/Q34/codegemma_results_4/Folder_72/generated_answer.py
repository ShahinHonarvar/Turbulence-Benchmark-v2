from functools import reduce

def find_original_set(sets):
    original_set = reduce(lambda a, b: a & b, sets)
    return original_set