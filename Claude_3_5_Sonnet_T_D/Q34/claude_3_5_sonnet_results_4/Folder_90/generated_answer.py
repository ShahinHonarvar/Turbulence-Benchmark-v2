def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('Function requires exactly 985 arguments')
    return set.union(*args)