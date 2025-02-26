def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Function requires exactly 63 distinct arguments')
    if len(set(map(frozenset, args))) != 63:
        raise ValueError('All arguments must be distinct')
    return set().union(*args)