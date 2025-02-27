def find_original_set(*args):
    set_union = set()
    for arg in args:
        set_union = set_union.union(arg)
    return set_union