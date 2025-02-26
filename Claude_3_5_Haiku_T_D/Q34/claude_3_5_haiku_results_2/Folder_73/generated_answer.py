def find_original_set(*sets):
    if len(sets) != 19:
        raise ValueError('Exactly 19 sets must be provided')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set