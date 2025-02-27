def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Function requires exactly 537 distinct arguments')
    return set.union(*args)