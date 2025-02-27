def find_original_set(*args):
    result = set()
    for i in range(702):
        result = result.union(args[i])
    return result