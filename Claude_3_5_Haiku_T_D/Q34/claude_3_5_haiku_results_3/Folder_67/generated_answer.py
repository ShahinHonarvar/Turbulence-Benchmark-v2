def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Function requires exactly 42 arguments')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set