def find_original_set(*args):
    if len(args) != 47:
        raise ValueError('Function takes exactly 47 distinct arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set')
        result_set.update(arg)
    return result_set