def find_original_set(*args):
    if len(args) != 69:
        raise ValueError('Function takes exactly 69 arguments')
    return set.union(*args)