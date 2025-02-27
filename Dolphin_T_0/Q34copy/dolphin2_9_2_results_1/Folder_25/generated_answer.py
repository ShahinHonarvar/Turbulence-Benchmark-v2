def find_original_set(*args):
    set_union = set()
    for s in args:
        set_union = set_union.union(s)
    return set_union