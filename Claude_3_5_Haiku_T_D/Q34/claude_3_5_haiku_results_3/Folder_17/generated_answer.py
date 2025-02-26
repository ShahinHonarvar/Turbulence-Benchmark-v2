def find_original_set(*sets):
    if len(sets) != 478:
        raise ValueError('Exactly 478 sets must be provided')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set