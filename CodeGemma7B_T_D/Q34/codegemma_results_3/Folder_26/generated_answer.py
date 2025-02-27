def find_original_set(*args):
    min_set = min(args, key=len)
    for arg in args:
        if not min_set.issuperset(arg):
            min_set.update(arg)
    return min_set