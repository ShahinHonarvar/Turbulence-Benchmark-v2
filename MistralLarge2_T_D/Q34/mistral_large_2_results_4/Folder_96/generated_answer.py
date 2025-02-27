def find_original_set(*sets):
    if len(sets) != 68:
        raise ValueError('Exactly 68 sets must be provided')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set