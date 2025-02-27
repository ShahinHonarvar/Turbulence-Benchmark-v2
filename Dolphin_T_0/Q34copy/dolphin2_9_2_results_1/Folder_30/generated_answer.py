def find_original_set(*args):
    if len(args) != 78:
        return 'Error: This function expects exactly 78 sets as arguments.'
    result = set()
    for arg in args:
        result = result.union(arg)
    return result