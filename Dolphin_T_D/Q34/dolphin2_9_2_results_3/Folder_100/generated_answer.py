def find_original_set(*args):
    result = set()
    for i in range(91):
        result = result.union(args[i])
    return result