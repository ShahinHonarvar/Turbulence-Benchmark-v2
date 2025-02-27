def find_original_set(*sets):
    if len(sets) != 27:
        raise ValueError('Exactly 27 distinct sets are required')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set