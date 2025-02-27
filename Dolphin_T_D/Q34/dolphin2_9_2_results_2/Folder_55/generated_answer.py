def find_original_set(*args):
    if len(args) != 33:
        raise ValueError('The function expects exactly 33 distinct arguments.')
    initial_set = set(args[0])
    for arg in args[1:]:
        initial_set = initial_set.union(arg)
    return initial_set