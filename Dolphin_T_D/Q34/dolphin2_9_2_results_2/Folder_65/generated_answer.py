def find_original_set(*args):
    if len(args) != 80:
        raise ValueError('Function must be called with exactly 80 distinct arguments')
    s = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets of integers')
        s |= arg
    return s