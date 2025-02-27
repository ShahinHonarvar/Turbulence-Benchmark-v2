def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Exactly 54 arguments are required')
    if len(set(args)) != 54:
        raise ValueError('All arguments must be distinct')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set