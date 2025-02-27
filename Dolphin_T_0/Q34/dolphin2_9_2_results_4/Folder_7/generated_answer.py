def find_original_set(*args):
    merge_set = set()
    for arg in args:
        if isinstance(arg, set):
            merge_set |= arg
    return merge_set