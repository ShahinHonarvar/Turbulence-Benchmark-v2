def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('Function requires exactly 415 arguments')
    return set().union(*args)