def find_original_set(*args):
    result_set = set()
    for i in range(len(args)):
        result_set = result_set.union(args[i])
    return result_set