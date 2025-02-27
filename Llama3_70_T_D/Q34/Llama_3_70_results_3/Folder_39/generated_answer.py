def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('Exactly 21 arguments are required')
    if len(set(map(frozenset, args))) != 21:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)