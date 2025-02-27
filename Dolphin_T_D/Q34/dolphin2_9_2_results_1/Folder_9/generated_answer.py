def find_original_set(*args):
    result = set(args[0])
    for i in range(1, 73):
        result = result.union(args[i])
    return result