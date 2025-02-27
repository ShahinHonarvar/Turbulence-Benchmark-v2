def find_original_set(*args):
    result_set = set()
    for subset in args:
        if not subset.issubset(result_set):
            result_set.update(subset)
    return result_set