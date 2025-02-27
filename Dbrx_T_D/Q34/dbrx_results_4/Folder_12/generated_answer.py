def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Function must take exactly 51 distinct arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set')
        result.update(arg)
    return result