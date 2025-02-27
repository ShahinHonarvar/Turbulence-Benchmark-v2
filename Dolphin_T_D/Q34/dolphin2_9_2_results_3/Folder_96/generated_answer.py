def find_original_set(*args):
    set_union = set()
    for i in range(68):
        set_union = set_union.union(args[i])
    return set_union