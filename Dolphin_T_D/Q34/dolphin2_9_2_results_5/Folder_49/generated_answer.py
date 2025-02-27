def find_original_set(*args):
    if len(args) != 60:
        return None
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set