from functools import reduce

def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 arguments are required.')
    return reduce(set.union, args)