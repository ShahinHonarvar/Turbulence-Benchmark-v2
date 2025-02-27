def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    original_set = set.union(*args)
    return original_set