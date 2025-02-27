def find_original_set(*args):
    if len(args) != 94:
        raise TypeError('find_original_set expected 94 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('all arguments must be sets')
        if len(arg) != len(set(arg)):
            raise ValueError('all sets must be distinct')
        original_set |= arg
    return original_set