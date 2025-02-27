def find_original_set(*args):
    if len(args) != 17:
        raise ValueError('Exactly 17 arguments are required.')
    return set().union(*args)