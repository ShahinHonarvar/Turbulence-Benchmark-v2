def find_original_set(*args):
    if len(args) != 34:
        raise ValueError('Exactly 34 arguments are required.')
    return set().union(*args)