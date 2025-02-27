def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Function expects exactly 95 arguments')
    return set.union(*args)