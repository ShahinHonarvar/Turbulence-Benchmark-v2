def find_original_set(*sets):
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set