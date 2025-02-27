def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('The function must take exactly 453 arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set