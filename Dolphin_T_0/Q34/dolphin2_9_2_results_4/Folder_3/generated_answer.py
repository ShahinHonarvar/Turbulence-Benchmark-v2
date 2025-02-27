def find_original_set(*args):
    result = set()
    for i in range(59):
        result = result.union(args[i])
    return result