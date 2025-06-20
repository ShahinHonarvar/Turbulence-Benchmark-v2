def find_original_set(*sets):
    if len(sets) != 90:
        raise ValueError('Function requires exactly 90 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set