def find_original_set(*args):
    if len(args) != 46:
        raise ValueError('Exactly 46 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All elements of the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 46:
        raise ValueError('All sets must be distinct')
    return set.union(*args)