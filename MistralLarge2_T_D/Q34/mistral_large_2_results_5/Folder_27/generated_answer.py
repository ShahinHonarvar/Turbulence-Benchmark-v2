def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Exactly 100 arguments are required.')
    return set.union(*args)