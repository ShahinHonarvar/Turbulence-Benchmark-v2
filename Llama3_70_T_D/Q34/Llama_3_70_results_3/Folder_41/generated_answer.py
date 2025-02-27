def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Exactly 20 arguments are required')
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(range(-2 ** 31, 2 ** 31)):
            raise ValueError('Each argument must be a set of integers')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set