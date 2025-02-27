def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 arguments must be provided.')
    if len(set(args)) != 85:
        raise ValueError('All arguments must be distinct.')
    result_set = set(args[0])
    for arg in args[1:]:
        result_set.update(arg)
    return result_set