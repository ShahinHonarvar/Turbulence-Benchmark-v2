def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('Exactly 23 distinct arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        if not arg.issubset(original_set):
            original_set = original_set.union(arg)
    return original_set