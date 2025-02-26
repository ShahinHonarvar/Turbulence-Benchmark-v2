def find_original_set(*args):
    if len(args) != 263:
        raise ValueError('Function must be called with exactly 263 arguments')
    return set().union(*args)