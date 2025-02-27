def find_original_set(*args):
    original_set = set()
    for subset in args:
        original_set = original_set.union(subset)
    return original_set