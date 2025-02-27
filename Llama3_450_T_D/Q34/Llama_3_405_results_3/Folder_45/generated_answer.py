def find_original_set(*args):
    if len(args) != 97:
        raise ValueError('Exactly 97 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(element, int) for arg in args for element in arg)):
        raise ValueError('All set elements must be integers')
    return set.union(*args)