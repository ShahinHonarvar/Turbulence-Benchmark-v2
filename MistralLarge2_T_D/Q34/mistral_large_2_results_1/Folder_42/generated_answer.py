def find_original_set(*sets):
    if len(sets) != 849:
        raise ValueError('Exactly 849 distinct arguments are required')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set