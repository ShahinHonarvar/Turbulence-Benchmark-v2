def find_original_set(*sets):
    if len(sets) != 34:
        raise ValueError('Function requires exactly 34 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set