def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('The function requires exactly 985 arguments.')
    return set.union(*args)