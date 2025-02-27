def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Function must take exactly 459 distinct arguments')
    result_set = set()
    for arg in args:
        if not all((item in arg for item in result_set)):
            raise ValueError('Not all arguments are subsets of the others')
        result_set.update(arg)
    return result_set