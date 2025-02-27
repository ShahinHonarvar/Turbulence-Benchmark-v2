from functools import reduce

def find_original_set(*args):

    def _reduce(a, b):
        return a & b
    return reduce(_reduce, args)