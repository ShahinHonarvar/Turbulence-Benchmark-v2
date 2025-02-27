def find_original_set(*args):
    if len(args) != 94:
        raise ValueError('Function must be called with exactly 94 arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements in sets must be integers.')
    original_set = set.union(*args)
    return original_set