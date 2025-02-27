def find_original_set(*args):
    if len(args) != 35:
        raise TypeError('find_original_set() takes exactly 35 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set |= arg
    return original_set