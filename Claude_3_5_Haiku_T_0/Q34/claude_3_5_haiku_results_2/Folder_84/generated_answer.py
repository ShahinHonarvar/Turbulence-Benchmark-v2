def find_original_set(*sets):
    if len(sets) != 132:
        raise ValueError('Function requires exactly 132 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set