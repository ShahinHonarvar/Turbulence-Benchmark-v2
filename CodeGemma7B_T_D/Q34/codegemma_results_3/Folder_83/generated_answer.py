def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('Exactly 64 arguments are required.')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
    return min(args, key=len)