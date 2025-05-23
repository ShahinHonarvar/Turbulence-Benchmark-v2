def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('The function requires exactly 415 distinct arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set