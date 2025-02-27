def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Function takes exactly 56 distinct arguments.')
    s = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers.')
        s = s.union(arg)
    return s