def find_original_set(*args):
    result = args[0]
    for cur_set in args[1:]:
        result = result.union(cur_set)
    return result