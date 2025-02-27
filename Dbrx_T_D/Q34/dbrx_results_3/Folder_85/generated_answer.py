def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 arguments are required')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set')
        result_set.update(arg)
    return result_set