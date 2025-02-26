def find_original_set(*sets):
    if len(sets) != 41:
        raise ValueError('Function must receive exactly 41 sets')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set