def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('Exactly 415 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        result_set = result_set.union(arg)
    return result_set