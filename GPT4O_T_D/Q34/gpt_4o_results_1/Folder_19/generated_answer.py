def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('Exactly 23 arguments are required')
    return set.union(*args)