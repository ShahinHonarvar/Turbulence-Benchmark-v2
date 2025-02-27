def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('The function expects exactly 415 arguments')
    result_set = set()
    for arg in args:
        if not all((val in arg for val in result_set)):
            raise ValueError('All arguments must be sets of integers')
        result_set.update(arg)
    return result_set