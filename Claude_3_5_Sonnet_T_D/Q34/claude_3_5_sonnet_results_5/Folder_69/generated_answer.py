def find_original_set(*args):
    if len(args) != 126:
        raise ValueError('Function requires exactly 126 arguments')
    return set().union(*args)