def find_original_set(*sets):
    if len(sets) != 95:
        raise ValueError('Exactly 95 sets are required')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set