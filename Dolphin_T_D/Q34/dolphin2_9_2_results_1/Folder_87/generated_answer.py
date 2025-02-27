def find_original_set(*args):
    if len(args) != 57:
        return 'Error: Wrong number of arguments'
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set