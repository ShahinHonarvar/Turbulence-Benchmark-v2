def find_original_set(*args):
    base_set = set()
    for s in args:
        base_set = base_set.union(s)
    return base_set