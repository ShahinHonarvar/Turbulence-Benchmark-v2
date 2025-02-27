def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Function must take exactly 276 distinct arguments')
    result_set = set()
    for arg in args:
        if not all((item in arg for item in result_set)):
            raise ValueError('All arguments must be sets of integers')
        result_set.update(arg)
    return result_set