def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Function requires exactly 99 arguments.')
    if len(set(args)) != 99:
        raise ValueError('Arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set