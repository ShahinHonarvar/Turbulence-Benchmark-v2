def find_original_set(*args):
    min_set = min(args, key=len)
    for arg in args:
        if not min_set.issuperset(arg):
            min_set = min((min_set, arg), key=len)
    return min_set