def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Function must take exactly 845 arguments')
    result = set()
    for arg in args:
        if not all((issubset(arg, result) for arg in args)):
            raise ValueError('All arguments must be distinct')
        result |= arg
    return result