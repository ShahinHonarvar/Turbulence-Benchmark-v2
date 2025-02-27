def find_original_set(*args):
    result = set()
    for set_arg in args:
        result = result.union(set_arg)
    return result