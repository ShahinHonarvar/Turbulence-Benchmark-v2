def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('Exactly 23 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    original_set = set.union(*args)
    return original_set