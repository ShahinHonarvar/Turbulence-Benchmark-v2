def find_original_set(*args):
    if len(args) != 33:
        raise ValueError('Exactly 33 arguments are required')
    return set().union(*args)