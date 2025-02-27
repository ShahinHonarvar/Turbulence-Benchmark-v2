def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Exactly 40 arguments are required')
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(range(-2 ** 31, 2 ** 31)):
            raise ValueError('All arguments must be sets of integers')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set