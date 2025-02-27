def find_original_set(*args):
    min_set = None
    for arg in args:
        if min_set is None or min_set.issuperset(arg):
            min_set = arg
    return min_set