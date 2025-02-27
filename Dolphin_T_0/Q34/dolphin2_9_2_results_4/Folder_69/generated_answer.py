def find_original_set(*args):
    original_set = set()
    for a in args:
        original_set = original_set.union(a)
    return original_set