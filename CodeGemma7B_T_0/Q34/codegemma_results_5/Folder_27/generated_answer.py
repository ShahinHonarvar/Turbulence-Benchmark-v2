def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('The function should take exactly 100 arguments')
    min_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments should be sets')
        min_set.update(s)
    for s in args:
        if not s.issubset(min_set):
            raise ValueError('All arguments should be subsets of the original set')
    return min_set