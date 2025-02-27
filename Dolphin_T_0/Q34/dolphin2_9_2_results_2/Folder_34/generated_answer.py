def find_original_set(*args):
    result = args[0]
    for set in args[1:]:
        result = result.union(set)
    return result