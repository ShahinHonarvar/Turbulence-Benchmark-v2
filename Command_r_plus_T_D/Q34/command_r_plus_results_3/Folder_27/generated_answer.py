def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Exactly 100 arguments are required.')
    if len(set(args)) != 100:
        raise ValueError('All arguments must be distinct.')
    smallest_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        smallest_set |= arg
    return smallest_set