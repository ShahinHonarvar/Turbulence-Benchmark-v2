def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('Exactly 45 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        original_set |= arg
    return original_set