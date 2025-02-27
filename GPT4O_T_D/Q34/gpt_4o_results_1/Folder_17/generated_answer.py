def find_original_set(*args):
    result_set = set()
    for subset in args:
        result_set.update(subset)
    return result_set