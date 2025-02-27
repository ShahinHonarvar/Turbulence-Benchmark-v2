def find_original_set(*args):
    if len(args) != 13:
        raise ValueError('The function must be called exactly 13 distinct sets of integers.')
    s = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('The function must be called with sets of integers.')
        if not arg.issubset(s):
            s = s.union(arg)
    return s