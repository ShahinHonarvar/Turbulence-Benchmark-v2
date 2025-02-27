def find_original_set(*args):
    if len(args) != 632:
        raise ValueError('Function takes exactly 632 arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set')
        result_set.update(arg)
    return result_set