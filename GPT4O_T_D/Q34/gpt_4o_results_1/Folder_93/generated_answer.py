def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('The function requires exactly 90 arguments.')
    return set.union(*args)