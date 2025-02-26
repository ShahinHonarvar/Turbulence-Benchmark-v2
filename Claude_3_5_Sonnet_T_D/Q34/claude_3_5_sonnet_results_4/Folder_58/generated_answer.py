def find_original_set(*args):
    if len(args) != 733:
        raise ValueError('Function expects exactly 733 arguments')
    return set().union(*args)