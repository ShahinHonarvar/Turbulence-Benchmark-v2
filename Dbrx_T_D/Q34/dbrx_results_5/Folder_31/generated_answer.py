def find_original_set(*args):
    if len(args) != 34:
        raise ValueError('Function expects exactly 34 arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set')
        for number in arg:
            if not isinstance(number, int):
                raise ValueError('Each set must contain only integers')
    union_set = set().union(*args)
    return union_set