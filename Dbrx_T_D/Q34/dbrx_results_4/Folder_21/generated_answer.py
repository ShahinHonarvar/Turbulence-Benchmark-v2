def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('This function expects exactly 851 distinct arguments')
    result_set = set()
    for arg in args:
        if not all((elem in arg for elem in result_set)):
            raise ValueError('Each of the given arguments must be a subset of the result')
        result_set.update(arg)
    return result_set