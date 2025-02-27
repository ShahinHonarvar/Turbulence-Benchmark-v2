def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('The function must take exactly 72 arguments.')
    if len(set(args)) != 72:
        raise ValueError('All arguments must be distinct.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set