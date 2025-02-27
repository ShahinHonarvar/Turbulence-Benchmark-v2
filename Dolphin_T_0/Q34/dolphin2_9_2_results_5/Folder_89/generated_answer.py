def find_original_set(*args):
    result_set = set()
    for arg in args:
        if isinstance(arg, set):
            result_set.update(arg)
    return result_set