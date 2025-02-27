def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Exactly 95 arguments are required')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set