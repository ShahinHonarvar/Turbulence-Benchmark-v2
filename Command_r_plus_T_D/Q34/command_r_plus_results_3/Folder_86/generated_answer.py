def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Exactly 162 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if arg in args[:args.index(arg)] or arg == result_set:
            raise ValueError('All arguments must be distinct sets.')
        result_set = result_set.union(arg)
    return result_set