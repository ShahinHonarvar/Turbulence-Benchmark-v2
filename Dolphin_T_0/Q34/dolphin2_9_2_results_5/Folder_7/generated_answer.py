def find_original_set(*args):
    result = None
    for arg in args:
        if result is None:
            result = arg
        else:
            result = result.union(arg)
    return result