def find_original_set(*sets):
    original_set = None
    for s in sets:
        if original_set is None or len(original_set) > len(s):
            original_set = s
    return original_set