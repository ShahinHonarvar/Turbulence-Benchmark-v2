def find_original_set(*args):
    if len(args) != 53:
        raise ValueError('Invalid number of arguments')
    min_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Invalid argument type')
        if len(min_set) == 0:
            min_set = arg
        else:
            min_set.update(arg)
    return min_set