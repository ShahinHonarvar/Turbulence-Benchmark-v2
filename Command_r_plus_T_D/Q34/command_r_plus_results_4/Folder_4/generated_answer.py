def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Exactly 40 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(num, int) for num in arg)) for arg in args)):
        raise TypeError('All elements in sets must be integers.')
    original_set = set.union(*args)
    return original_set