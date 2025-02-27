def find_original_set(arg):
    original_set = set()
    for subset in arg:
        if not subset.issubset(original_set):
            original_set = original_set.union(subset)
    return original_set