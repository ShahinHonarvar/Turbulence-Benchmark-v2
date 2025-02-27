def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Exactly 72 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if arg in args[:args.index(arg)] + args[args.index(arg) + 1:]:
            raise ValueError('All arguments must be distinct sets.')
        result_set |= arg
    return result_set