def find_original_set(*sets):
    if len(sets) != 24:
        raise ValueError('Function requires exactly 24 distinct sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set