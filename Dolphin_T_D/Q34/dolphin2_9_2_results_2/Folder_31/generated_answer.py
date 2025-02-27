def find_original_set(*args):
    if len(args) != 34:
        raise ValueError('Function expects exactly 34 distinct arguments.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set