def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Exactly 40 arguments are required.')
    return set.union(*args)