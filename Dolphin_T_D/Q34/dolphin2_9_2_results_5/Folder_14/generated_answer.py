def find_original_set(*args):
    if len(args) != 13:
        raise ValueError('This function expects exactly 13 arguments.')
    return set.union(*args)