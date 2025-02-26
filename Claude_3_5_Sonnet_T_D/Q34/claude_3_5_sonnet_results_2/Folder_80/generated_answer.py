def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Function requires exactly 453 arguments')
    return set().union(*args)