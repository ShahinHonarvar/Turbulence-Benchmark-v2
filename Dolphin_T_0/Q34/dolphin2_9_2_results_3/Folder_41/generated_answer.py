def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Function must have exactly 20 arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Args must be sets of integers.')
        original_set = original_set.union(arg)
    return original_set