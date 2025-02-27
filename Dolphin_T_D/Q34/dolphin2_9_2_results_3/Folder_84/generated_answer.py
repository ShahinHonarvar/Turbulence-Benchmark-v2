def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('This function must be called with exactly 132 arguments, each of which is a set of integers.')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each of the 132 arguments must be a set of integers.')
        if not arg.issubset(result):
            result |= arg
    return result