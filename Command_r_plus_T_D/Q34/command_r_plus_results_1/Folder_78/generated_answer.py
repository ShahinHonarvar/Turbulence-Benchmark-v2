def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Exactly 48 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if arg == result_set:
            raise ValueError('All sets must be distinct.')
        result_set = result_set.union(arg)
    return result_set