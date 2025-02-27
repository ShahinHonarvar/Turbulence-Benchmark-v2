def find_original_set(*args):
    result_set = set()
    for argument_set in args:
        result_set = result_set.union(argument_set)
    return result_set