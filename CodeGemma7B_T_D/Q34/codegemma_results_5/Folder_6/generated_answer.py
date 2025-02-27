from functools import reduce

def find_original_set(*args):
    return reduce(set.intersection, args)