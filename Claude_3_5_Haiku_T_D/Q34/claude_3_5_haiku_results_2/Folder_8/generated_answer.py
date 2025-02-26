def find_original_set(*sets):
    if len(sets) != 45:
        raise ValueError('Function requires exactly 45 sets')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set