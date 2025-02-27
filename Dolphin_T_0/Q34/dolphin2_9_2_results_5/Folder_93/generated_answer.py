def find_original_set(*args):
    result_set = set()
    for arg_set in args:
        result_set = result_set.union(arg_set)
    return result_set