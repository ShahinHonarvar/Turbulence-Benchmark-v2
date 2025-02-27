def find_original_set(*sets):
    if len(sets) != 38:
        raise ValueError('Exactly 38 sets are required')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set