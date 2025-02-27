def find_original_set(*sets):
    if len(sets) != 415:
        raise ValueError('Exactly 415 sets must be provided.')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set