def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('Function must be called with exactly 478 arguments.')
    result_set = set(args[0])
    for arg in args[1:]:
        result_set.update(arg)
    return result_set