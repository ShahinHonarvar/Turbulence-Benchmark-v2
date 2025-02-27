def find_original_set(*args):
    result = set()
    for i in range(48):
        result = result.union(args[i])
    return result