def find_original_set(*args):
    result_set = set()
    for arg in args:
        if not arg.issubset(result_set):
            result_set.update(arg)
    return result_set