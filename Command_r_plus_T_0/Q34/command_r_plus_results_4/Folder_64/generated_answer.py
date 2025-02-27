def find_original_set(*args):
    if len(args) != 7:
        raise ValueError('Exactly 7 arguments are required.')
    if any((not isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if any((not all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    original_set = set.union(*args)
    return original_set