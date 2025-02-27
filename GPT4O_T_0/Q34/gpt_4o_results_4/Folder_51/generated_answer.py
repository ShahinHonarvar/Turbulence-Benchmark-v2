def find_original_set(*args):
    if len(args) != 28:
        raise ValueError('Exactly 28 arguments are required')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set