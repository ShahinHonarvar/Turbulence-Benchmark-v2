def find_original_set(*args):
    if len(args) != 43:
        raise ValueError('Exactly 43 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(original_set):
            original_set = original_set.union(arg)
    return original_set