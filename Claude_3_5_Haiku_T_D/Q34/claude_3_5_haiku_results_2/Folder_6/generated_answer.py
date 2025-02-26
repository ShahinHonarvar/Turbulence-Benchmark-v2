def find_original_set(*sets):
    if len(sets) != 276:
        raise ValueError('Function requires exactly 276 distinct sets')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set