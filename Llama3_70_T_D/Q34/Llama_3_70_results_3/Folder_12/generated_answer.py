def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Exactly 51 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        original_set = original_set.union(arg)
    return original_set