def find_original_set(*args):
    if len(args) != 84:
        raise TypeError('find_original_set() takes exactly 84 arguments')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set