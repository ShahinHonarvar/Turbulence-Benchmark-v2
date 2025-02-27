def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((arg.issubset(int) for arg in args)):
        raise ValueError('All elements of the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 99:
        raise ValueError('All sets must be distinct')
    return set.union(*args)