def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Function takes exactly 49 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        original_set |= arg
    return original_set