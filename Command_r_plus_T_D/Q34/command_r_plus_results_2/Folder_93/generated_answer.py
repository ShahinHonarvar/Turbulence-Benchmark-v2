def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Function must be called with exactly 90 arguments.')
    if len(set(args)) != 90:
        raise ValueError('All arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set