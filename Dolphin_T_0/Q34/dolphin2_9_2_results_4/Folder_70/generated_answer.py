def find_original_set(*args):
    result_set = set()
    for input_set in args:
        result_set = result_set.union(input_set)
    return result_set