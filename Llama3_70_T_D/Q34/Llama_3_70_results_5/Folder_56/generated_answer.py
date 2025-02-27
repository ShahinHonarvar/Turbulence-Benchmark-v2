def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Exactly 63 arguments are required')
    if len(set((tuple(sorted(arg)) for arg in args))) != 63:
        raise ValueError('Each argument must be distinct')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('Each argument must be a set of integers')
    result = set()
    for arg in args:
        result |= arg
    return result