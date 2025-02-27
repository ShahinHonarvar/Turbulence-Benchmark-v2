def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Exactly 312 arguments are required.')
    return set.union(*args)