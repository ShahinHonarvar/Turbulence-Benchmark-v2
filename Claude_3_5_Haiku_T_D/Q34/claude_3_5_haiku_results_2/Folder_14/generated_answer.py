def find_original_set(*sets):
    if len(sets) != 13:
        raise ValueError('Function must be called with exactly 13 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set