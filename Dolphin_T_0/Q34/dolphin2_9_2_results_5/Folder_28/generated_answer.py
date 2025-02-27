def find_original_set(*args):
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set')
        result = result.union(arg)
    return result