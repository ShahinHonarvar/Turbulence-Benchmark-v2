def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Exactly 194 arguments are required.')
    return set.union(*args)