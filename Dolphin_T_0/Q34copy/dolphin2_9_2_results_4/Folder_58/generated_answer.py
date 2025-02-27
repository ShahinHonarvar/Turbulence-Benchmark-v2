def find_original_set(*args):
    result_set = set()
    for argument in args:
        result_set = result_set.union(argument)
    return result_set