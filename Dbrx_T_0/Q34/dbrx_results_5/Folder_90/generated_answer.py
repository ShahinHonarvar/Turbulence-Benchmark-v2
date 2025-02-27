def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('Function must take exactly 985 distinct arguments')
    result_set = set()
    for arg in args:
        if not all((item in arg for item in result_set)):
            raise ValueError('Each argument must be a subset of the original set')
        result_set.update(arg)
    return result_set