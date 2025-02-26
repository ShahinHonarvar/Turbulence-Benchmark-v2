def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Function requires exactly 845 arguments')
    return set().union(*args)