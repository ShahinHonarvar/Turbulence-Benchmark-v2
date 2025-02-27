def find_original_set(*args):
    original_set = set()
    for i in args:
        original_set = original_set.union(i)
    return original_set