def find_original_set(*args):
    if len(args) != 733:
        raise ValueError('Function requires exactly 733 arguments')
    return set().union(*args)