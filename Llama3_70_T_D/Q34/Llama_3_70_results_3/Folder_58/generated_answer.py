def find_original_set(*sets):
    if len(sets) != 733:
        raise ValueError('Exactly 733 arguments are required')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set