def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('The function must take exactly 88 arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set