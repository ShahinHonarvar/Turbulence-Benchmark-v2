def find_original_set(*args):
    if len(set(args)) != 45:
        raise ValueError('The function must take exactly 45 distinct arguments.')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set