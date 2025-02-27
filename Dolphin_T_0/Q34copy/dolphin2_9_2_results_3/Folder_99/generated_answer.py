def find_original_set(*sets):
    merged_set = sets[0]
    for set in sets[1:]:
        merged_set = merged_set.union(set)
    for set in sets:
        if not set.issubset(merged_set):
            return None
    return merged_set