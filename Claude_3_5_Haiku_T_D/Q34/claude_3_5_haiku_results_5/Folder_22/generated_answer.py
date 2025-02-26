def find_original_set(*sets):
    original_set = set()
    for current_set in sets:
        original_set.update(current_set)
    return original_set