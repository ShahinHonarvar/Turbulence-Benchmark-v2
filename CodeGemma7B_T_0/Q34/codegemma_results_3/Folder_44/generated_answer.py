def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Invalid number of arguments')
    min_set = set()
    for s in args:
        min_set.update(s)
    for s in args:
        if not s.issubset(min_set):
            raise ValueError('Not all sets are subsets of the original set')
    return min_set