def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Exactly 67 arguments are required')
    result_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets')
        result_set.update(s)
    return result_set