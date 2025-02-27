def find_original_set(*args):
    if len(args) != 321:
        raise TypeError('find_original_set expected 321 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set |= arg
    return original_set