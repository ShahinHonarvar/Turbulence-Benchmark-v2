def find_original_set(*args):
    if len(args) != 42:
        raise TypeError('Expected 42 arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set