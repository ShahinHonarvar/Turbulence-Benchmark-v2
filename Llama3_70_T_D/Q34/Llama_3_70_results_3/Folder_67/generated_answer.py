def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Exactly 42 arguments are required')
    if len(set(map(tuple, args))) != 42:
        raise ValueError('All 42 arguments must be distinct')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set