def find_original_set(*args):
    original_set = set(args[0])
    for s in args:
        original_set = original_set.union(s)
    return original_set