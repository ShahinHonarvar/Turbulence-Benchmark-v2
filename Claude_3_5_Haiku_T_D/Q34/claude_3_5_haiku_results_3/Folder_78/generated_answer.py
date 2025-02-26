def find_original_set(*sets):
    if len(sets) != 48:
        raise ValueError('Exactly 48 sets must be provided')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set