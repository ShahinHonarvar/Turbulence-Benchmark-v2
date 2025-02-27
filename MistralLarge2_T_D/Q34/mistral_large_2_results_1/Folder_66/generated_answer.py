def find_original_set(*args):
    if len(args) != 25:
        raise ValueError('Exactly 25 arguments are required.')
    return set().union(*args)