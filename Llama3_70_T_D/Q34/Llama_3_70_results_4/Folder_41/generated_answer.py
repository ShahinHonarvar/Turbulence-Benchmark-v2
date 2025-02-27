def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Exactly 20 arguments are required')
    if len(set(map(frozenset, args))) != 20:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)