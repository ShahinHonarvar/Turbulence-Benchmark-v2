def find_original_set(*sets):
    if len(sets) != 5:
        raise ValueError('Function requires exactly 5 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set