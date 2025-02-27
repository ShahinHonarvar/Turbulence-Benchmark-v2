def find_original_set(*args):
    result_set = set()
    for a in args:
        result_set = result_set.union(a)
    return result_set