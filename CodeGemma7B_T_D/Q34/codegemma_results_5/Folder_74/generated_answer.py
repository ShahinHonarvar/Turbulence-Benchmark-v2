def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Invalid number of arguments')
    min_set = set(range(97))
    for arg in args:
        if not arg.issubset(min_set):
            min_set = min_set.union(arg)
    return min_set