def find_original_set(*sets):
    max_set = set()
    for s in sets:
        if len(s) > len(max_set):
            max_set = s
    if len(max_set) == len(sets):
        return None
    for s in sets:
        if s != max_set:
            max_set.intersection_update(s)
    return max_set