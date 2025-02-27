def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Exactly 27 arguments are required')
    if len(set(map(id, args))) != 27:
        raise ValueError('All arguments must be distinct')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements of the sets must be integers')
    return set.union(*args)