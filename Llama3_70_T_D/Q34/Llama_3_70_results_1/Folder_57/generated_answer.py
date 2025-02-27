def find_original_set(*args):
    if len(args) != 93:
        raise ValueError('Exactly 93 arguments required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements in the sets must be integers')
    return set.union(*args)