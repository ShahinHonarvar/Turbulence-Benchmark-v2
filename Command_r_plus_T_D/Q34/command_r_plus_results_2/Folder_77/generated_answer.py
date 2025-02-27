def find_original_set(*args):
    result_set = set(args[0])
    for arg in args[1:]:
        result_set.update(arg)
    return result_set