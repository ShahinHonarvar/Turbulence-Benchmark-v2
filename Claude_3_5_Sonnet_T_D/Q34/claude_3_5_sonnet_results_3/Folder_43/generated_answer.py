def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Function requires exactly 49 distinct arguments')
    if len(set(map(frozenset, args))) != 49:
        raise ValueError('All arguments must be distinct')
    return set().union(*args)