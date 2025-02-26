def find_original_set(*sets):
    if len(sets) != 84:
        raise ValueError('Function requires exactly 84 sets')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set