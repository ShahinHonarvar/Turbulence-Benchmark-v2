def find_original_set(*args):
    original_set = set()
    for lst in args:
        original_set = original_set.union(lst)
    return original_set