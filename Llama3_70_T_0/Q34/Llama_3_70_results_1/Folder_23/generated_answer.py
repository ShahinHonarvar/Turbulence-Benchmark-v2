def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('Exactly 41 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements in the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 41:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)