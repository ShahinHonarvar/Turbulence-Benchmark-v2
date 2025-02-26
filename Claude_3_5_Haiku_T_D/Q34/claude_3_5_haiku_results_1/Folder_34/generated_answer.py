def find_original_set(*sets):
    merged_set = set()
    for s in sets:
        merged_set.update(s)
    return merged_set