def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Exactly 537 arguments are required')
    return set.union(*args)