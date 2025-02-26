def find_original_set(*sets):
    if len(sets) != 28:
        raise ValueError('Exactly 28 sets are required')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set