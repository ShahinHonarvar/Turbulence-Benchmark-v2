def find_original_set(*sets):
    if len(sets) != 47:
        raise ValueError('Function must be called with exactly 47 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set