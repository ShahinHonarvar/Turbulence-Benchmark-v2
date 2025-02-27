def find_original_set(*args):
    result_set = set.union(*args)
    for input_set in args:
        if not input_set.issubset(result_set):
            result_set.update(input_set)
    return result_set