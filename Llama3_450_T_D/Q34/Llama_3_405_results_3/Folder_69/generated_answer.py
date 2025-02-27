def find_original_set(*args):
    if len(args) != 126:
        raise TypeError('Expected exactly 126 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise TypeError('All elements of the sets must be integers')
    return set.union(*args)