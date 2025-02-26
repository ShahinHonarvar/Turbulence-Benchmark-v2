def find_original_set(*args):
    if len(args) != 746:
        raise ValueError('Function requires exactly 746 arguments')
    return set().union(*args)