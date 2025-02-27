def find_original_set(*args):
    if len(args) != 59:
        raise ValueError('Exactly 59 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements of the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 59:
        raise ValueError('All sets must be distinct')
    return set.union(*args)