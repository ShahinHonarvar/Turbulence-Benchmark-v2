def find_original_set(*args):
    result = {}
    for _ in range(20):
        result = result.union(args[_])
    return result