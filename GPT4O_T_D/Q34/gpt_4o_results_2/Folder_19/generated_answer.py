def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('The function requires exactly 23 arguments')
    return set().union(*args)