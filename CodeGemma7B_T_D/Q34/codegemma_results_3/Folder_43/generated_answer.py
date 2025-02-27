from functools import reduce

def find_original_set(*sets):
    return reduce(min, sets, sets[0])