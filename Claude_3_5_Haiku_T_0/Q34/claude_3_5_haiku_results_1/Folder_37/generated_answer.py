def find_original_set(*sets):
    if len(sets) != 67:
        raise ValueError('Function requires exactly 67 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set