def find_original_set(*sets):
    if len(sets) != 453:
        raise ValueError('Function requires exactly 453 sets')
    original_set = set()
    for current_set in sets:
        original_set.update(current_set)
    return original_set