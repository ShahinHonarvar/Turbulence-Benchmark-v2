def find_original_set(*args):
    if len(args) != 38:
        raise ValueError('Exactly 38 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All set items must be integers.')
    original_set = set.union(*args)
    return original_set