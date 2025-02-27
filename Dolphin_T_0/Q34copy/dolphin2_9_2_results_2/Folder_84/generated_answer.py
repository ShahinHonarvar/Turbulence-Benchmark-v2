def find_original_set(*args):
    result_set = set()
    for given_set in args:
        result_set.update(given_set)
    return result_set