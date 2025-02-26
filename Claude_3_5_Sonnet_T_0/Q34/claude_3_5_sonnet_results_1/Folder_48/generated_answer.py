def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function requires exactly 990 arguments')
    return set().union(*args)