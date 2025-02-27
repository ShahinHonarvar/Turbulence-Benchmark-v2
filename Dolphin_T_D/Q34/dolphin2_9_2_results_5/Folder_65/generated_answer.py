def find_original_set(*args):
    result = set()
    for i in range(80):
        result = result.union(args[i])
    return result