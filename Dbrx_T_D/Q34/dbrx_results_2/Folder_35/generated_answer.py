def find_original_set(*args):
    if len(args) != 702:
        raise ValueError('Function takes exactly 702 arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        for element in arg:
            if not isinstance(element, int):
                raise ValueError('All sets must contain only integers')
        result_set |= arg
    return result_set