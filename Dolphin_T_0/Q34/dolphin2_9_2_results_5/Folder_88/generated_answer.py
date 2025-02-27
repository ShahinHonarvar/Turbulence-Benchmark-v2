def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Invalid number of arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Invalid argument type')
        result |= arg
    return result