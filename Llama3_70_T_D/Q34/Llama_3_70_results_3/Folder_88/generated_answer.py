def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Exactly 27 arguments are required')
    if len(set((frozenset(arg) for arg in args))) != 27:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)