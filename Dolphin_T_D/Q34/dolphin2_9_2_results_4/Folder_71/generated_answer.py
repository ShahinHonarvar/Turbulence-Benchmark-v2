def find_original_set(*args):
    s_union = set()
    for s in args:
        s_union = s_union.union(s)
    return s_union