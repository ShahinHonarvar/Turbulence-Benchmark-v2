def find_original_set(*args):
    if len(args) != 34:
        raise ValueError('Exactly 34 arguments required')
    return set.union(*args)