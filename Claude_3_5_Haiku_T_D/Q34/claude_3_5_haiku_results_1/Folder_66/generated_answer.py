def find_original_set(*args):
    if len(args) != 25:
        raise ValueError('Function must be called with exactly 25 sets')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set