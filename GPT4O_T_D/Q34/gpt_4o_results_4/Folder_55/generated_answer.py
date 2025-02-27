def find_original_set(*args):
    result_set = set()
    for current_set in args:
        result_set.update(current_set)
    return result_set