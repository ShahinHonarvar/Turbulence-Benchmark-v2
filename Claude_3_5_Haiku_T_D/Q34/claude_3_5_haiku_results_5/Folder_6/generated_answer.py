def find_original_set(*sets):
    if len(sets) != 276:
        raise ValueError('Exactly 276 sets must be provided')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set