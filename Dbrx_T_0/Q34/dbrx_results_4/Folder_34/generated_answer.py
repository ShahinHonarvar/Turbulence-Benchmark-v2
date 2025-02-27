def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Function takes exactly 95 arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        result_set.update(arg)
    return result_set