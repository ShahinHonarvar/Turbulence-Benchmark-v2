def find_original_set(*args):
    if len(args) != 194:
        return None
    result = set()
    for arg in args:
        result = result.union(arg)
    return result