def find_original_set(*args):
    if len(args) != 93:
        raise ValueError('Function requires exactly 93 arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in sets must be integers.')
    original_set = set.union(*args)
    return original_set