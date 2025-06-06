def find_original_set(*sets):
    if len(sets) != 84:
        raise ValueError('Function requires exactly 84 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set