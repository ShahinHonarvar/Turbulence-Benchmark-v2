def find_original_set(*args):
    if len(args) != 453:
        raise TypeError('Expected 453 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise TypeError('All elements of the sets must be integers')
    return set.union(*args)