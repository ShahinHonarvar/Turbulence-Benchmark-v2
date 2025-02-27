def find_original_set(*args):
    if len(args) != 74:
        raise ValueError('The function must be called with 74 arguments.')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set