def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('Exactly 21 arguments are required.')
    if len(set(args)) != 21:
        raise ValueError('All arguments must be distinct.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set