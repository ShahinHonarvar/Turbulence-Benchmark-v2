def find_original_set(*sets):
    if len(sets) != 21:
        raise ValueError('Exactly 21 sets are required')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set