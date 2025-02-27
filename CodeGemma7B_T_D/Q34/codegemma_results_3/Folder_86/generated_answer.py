from functools import reduce

def find_original_set(*args):
    return reduce(lambda a, b: a & b, args)