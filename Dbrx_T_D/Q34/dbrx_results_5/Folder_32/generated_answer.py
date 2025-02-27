def find_original_set(sets):
    all_elements = set()
    for s in sets:
        all_elements = all_elements | s
    return all_elements