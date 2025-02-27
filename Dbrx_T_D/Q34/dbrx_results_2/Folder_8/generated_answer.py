def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('45 distinct arguments required')
    union_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        union_set.update(arg)
    return union_set