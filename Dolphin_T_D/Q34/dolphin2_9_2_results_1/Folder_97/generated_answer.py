def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Function must be called with exactly 194 distinct arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Arguments must be sets of integers.')
        original_set = original_set.union(arg)
    return original_set