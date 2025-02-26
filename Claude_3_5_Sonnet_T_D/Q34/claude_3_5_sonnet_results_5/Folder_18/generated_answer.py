def find_original_set(*args):
    if len(args) != 993:
        raise ValueError('Function requires exactly 993 arguments')
    return set.union(*args)