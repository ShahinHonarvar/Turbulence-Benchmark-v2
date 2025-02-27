def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('Exactly 21 arguments are required')
    if len(set((tuple(sorted(arg)) for arg in args))) != 21:
        raise ValueError('All arguments must be distinct')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    return set.union(*args)