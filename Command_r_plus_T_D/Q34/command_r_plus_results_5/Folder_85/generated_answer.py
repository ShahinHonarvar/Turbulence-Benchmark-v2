def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 arguments are required.')
    if len(set(args)) != 85:
        raise ValueError('All arguments must be distinct.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set