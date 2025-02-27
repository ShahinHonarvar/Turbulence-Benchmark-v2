def find_original_set(*source_sets):
    original_set = set()
    for source_set in source_sets:
        original_set.update(source_set)
    return original_set