def find_original_set(*args):
    if len(set(args)) != 45:
        raise ValueError('The function must have exactly 45 distinct arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set