def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Function requires exactly 24 distinct sets')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set