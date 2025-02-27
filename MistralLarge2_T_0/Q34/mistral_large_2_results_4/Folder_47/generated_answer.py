def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments are required.')
    return set.union(*args)