def find_original_set(*sets):
    if len(sets) != 247:
        raise ValueError('This function requires exactly 247 sets.')
    original_set = set()
    for s in sets:
        original_set = original_set.union(s)
    return original_set