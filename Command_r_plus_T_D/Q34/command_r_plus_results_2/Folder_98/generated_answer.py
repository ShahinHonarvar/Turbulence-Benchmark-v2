def find_original_set(*args):
    if len(args) != 9:
        raise ValueError('Exactly 9 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((isinstance(x, int) for x in arg)):
            raise ValueError('All elements in the sets must be integers.')
        original_set |= arg
    return original_set