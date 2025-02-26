def find_original_set(*sets):
    if len(sets) != 247:
        raise ValueError('Function requires exactly 247 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set