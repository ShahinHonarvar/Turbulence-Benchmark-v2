def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Function requires exactly 926 arguments')
    return set().union(*args)