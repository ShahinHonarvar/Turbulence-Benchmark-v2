def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('Function must be called with exactly 15 sets')
    original_set = set()
    for arg_set in args:
        if not isinstance(arg_set, set):
            raise TypeError('All arguments must be sets')
        original_set.update(arg_set)
    return original_set