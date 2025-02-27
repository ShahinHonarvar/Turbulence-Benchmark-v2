def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Function requires exactly 99 arguments.')
    if len(set(args)) != 99:
        raise ValueError('All arguments must be distinct.')
    original_set = set.union(*args)
    return original_set