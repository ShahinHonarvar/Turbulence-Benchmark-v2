def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('Invalid number of arguments')
    min_set = set()
    for s in args:
        min_set.update(s)
    return min_set