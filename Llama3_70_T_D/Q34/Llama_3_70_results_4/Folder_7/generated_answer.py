def find_original_set(*args):
    if len(args) != 537:
        raise TypeError('find_original_set() takes exactly 537 arguments')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set