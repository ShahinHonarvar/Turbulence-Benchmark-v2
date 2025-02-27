def find_original_set(*args):
    union = set()
    for s in args:
        union = union.union(s)
    return union