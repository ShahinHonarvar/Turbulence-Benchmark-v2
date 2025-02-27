def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 arguments are required.')
    if len(set(args)) != 85:
        raise ValueError('All arguments must be distinct.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        original_set |= arg
    return original_set