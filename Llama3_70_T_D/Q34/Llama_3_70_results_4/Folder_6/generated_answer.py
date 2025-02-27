def find_original_set(*args):
    if len(args) != 276:
        raise TypeError('Exactly 276 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(range(-2 ** 31, 2 ** 31)):
            raise TypeError('All elements in the sets must be integers')
        original_set |= arg
    return original_set