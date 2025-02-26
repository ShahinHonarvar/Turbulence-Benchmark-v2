def find_original_set(*sets):
    if len(sets) != 15:
        raise ValueError('Function requires exactly 15 sets')
    unique_sets = set(sets)
    if len(unique_sets) != 15:
        raise ValueError('All 15 sets must be distinct')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set