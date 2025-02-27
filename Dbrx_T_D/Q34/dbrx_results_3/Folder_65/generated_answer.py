def find_original_set(*args):
    if len(args) != 80:
        raise ValueError('Function requires exactly 80 distinct arguments')
    result_set = set()
    for arg in args:
        if not all((item in arg for item in result_set)):
            raise ValueError('All provided sets must be subsets of the result')
        result_set.update(arg)
    return result_set