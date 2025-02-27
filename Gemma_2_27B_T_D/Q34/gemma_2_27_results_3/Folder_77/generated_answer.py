def find_original_set(*sets):
    original_set = set()
    for subset in sets:
        original_set = original_set.union(subset)
    return original_set