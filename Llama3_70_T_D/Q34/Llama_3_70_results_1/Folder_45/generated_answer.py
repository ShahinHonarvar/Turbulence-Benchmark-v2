def find_original_set(*args):
    if len(args) != 97:
        raise TypeError('Expected exactly 97 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(original_set):
            original_set |= arg
    return original_set