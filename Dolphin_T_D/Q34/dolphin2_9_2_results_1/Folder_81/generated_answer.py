def find_original_set(*args):
    result_set = set(args[0])
    for s in args[1:]:
        result_set = result_set.union(s)
    return result_set