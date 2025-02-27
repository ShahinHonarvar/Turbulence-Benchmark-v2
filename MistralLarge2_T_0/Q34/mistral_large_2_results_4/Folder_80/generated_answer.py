def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Exactly 453 arguments are required.')
    return set.union(*args)