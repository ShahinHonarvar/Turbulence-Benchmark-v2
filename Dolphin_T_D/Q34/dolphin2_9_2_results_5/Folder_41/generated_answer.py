def find_original_set(*args):
    result = set()
    for i in range(len(args)):
        result = result.union(args[i])
    return result