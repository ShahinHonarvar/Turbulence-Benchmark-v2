def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Exactly 48 arguments are required.')
    result_set = set().union(*args)
    for arg in args:
        if not arg.issubset(result_set):
            raise ValueError('All arguments must be subsets of the original set.')
    return result_set