def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Function takes exactly 27 arguments')
    union_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers')
        union_set.update(arg)
    return union_set