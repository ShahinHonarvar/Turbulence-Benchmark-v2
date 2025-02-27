def find_original_set(*args):
    if len(args) != 27:
        raise TypeError('The function must have exactly 27 distinct arguments.')
    result = set()
    for arg in args:
        result = result.union(arg)
    return result