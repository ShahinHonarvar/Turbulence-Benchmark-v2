def find_original_set(*args):
    result = set()
    for single_arg in args:
        result = result.union(single_arg)
    return result