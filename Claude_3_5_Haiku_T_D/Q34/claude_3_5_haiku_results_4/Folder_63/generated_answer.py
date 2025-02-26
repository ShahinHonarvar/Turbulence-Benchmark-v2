def find_original_set(*sets):
    if len(sets) != 18:
        raise ValueError('Exactly 18 sets must be provided')
    original_set = set()
    for current_set in sets:
        original_set.update(current_set)
    return original_set