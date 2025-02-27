def find_original_set(*args):
    if len(args) != 7:
        raise ValueError('This function requires exactly 7 arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set