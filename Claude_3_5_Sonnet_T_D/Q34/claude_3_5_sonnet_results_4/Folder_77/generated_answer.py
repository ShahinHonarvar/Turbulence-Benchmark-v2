def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('Function requires exactly 410 arguments')
    return set().union(*args)