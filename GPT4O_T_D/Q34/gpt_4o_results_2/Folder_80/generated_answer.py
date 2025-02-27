def find_original_set(*sets):
    if len(sets) != 453:
        raise ValueError('Exactly 453 sets required')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set