from functools import reduce

def find_original_set(*args):
    return reduce(lambda x, y: x & y, args)