def find_original_set(*args):
    if len(args) != 66:
        raise ValueError('Exactly 66 arguments are required')
    if len(set(map(tuple, args))) != 66:
        raise ValueError('All 66 arguments must be distinct')
    if not all((isinstance(arg, set) and arg.issubset(range(-2 ** 31, 2 ** 31)) for arg in args)):
        raise ValueError('Each argument must be a set of integers')
    return set.union(*args)