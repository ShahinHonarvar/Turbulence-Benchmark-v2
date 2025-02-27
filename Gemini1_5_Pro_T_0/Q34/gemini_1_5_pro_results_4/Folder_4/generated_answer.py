def find_original_set(*args):
    if len(set(args)) != 40:
        raise ValueError('The 40 arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set