def find_original_set(*args):
    union_set = set()
    for s in args:
        union_set = union_set.union(s)
    return union_set