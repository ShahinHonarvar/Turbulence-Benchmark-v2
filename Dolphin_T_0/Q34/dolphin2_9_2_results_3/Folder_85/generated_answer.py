def find_original_set(*args):
    if len(args) != 85:
        return None
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(original_set):
            return None
        original_set = original_set.union(arg)
    return original_set