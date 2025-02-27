def find_original_set(*sets):
    if len(sets) != 790:
        raise ValueError('Exactly 790 distinct arguments are required.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set