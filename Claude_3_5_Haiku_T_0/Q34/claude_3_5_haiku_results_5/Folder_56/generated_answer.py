def find_original_set(*sets):
    if len(sets) != 63:
        raise ValueError('Function requires exactly 63 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set