def find_original_set(*args):
    if len(args) != 92:
        raise ValueError('Function requires exactly 92 arguments.')
    return set.union(*args)