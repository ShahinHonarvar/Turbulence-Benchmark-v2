def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Exactly 845 arguments are required.')
    return set.union(*args)