def find_original_set(*sets):
    combined_set = set()
    for s in sets:
        combined_set = combined_set.union(s)
    return combined_set