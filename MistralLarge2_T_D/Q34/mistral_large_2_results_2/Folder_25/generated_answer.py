def find_original_set(*args):
    if len(args) != 38:
        raise ValueError('Exactly 38 arguments are required.')
    return set.union(*args)