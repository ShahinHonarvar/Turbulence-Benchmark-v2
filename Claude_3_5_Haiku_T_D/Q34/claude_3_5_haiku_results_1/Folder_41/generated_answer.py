def find_original_set(*sets):
    if len(sets) != 20:
        raise ValueError('Exactly 20 sets must be provided')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set