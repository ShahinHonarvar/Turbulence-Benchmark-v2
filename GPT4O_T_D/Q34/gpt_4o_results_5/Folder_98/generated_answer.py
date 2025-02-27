def find_original_set(*args):
    if len(args) != 9:
        raise ValueError('Exactly 9 arguments are required.')
    return set().union(*args)