def find_original_set(*args):
    if len(args) != 73:
        raise ValueError('Exactly 73 arguments are required.')
    return set.union(*args)