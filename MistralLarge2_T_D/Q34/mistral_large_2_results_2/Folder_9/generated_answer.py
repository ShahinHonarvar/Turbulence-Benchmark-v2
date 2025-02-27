def find_original_set(*sets):
    if len(sets) != 73:
        raise ValueError('Exactly 73 sets must be provided.')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set