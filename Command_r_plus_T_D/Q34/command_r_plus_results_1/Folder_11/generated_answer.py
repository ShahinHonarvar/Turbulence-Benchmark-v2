def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Exactly 54 arguments are required.')
    if len(args) != len(set(args)):
        raise ValueError('Arguments must be distinct.')
    result_set = set()
    for arg_set in args:
        result_set.update(arg_set)
    return result_set