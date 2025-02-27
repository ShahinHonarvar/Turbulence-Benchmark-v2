def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Exactly 714 arguments are required.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        result_set.update(arg)
    return result_set