def find_original_set(*args):
    if len(set(args)) != 77:
        raise ValueError('The function must take exactly 77 distinct arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set