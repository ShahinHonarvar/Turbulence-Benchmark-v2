def find_original_set(*args):
    union_set = set()
    for arg in args:
        union_set.update(arg)
    return union_set