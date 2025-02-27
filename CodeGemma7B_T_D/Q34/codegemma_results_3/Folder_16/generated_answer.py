def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('Wrong number of arguments')
    original_set = min(args, key=len)
    for s in args:
        if not s.issubset(original_set):
            raise ValueError('Not all sets are subsets')
    return original_set