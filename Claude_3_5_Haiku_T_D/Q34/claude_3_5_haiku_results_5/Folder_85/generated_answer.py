def find_original_set(*sets):
    if len(sets) != 85:
        raise ValueError('Exactly 85 sets must be provided')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set