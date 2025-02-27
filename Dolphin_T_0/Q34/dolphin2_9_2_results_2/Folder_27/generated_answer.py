def find_original_set(*args):
    result_set = set()
    for group in args:
        result_set = result_set.union(group)
    return result_set