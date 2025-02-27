def find_original_set(*sets):
    if len(sets) != 63:
        raise ValueError('The function requires exactly 63 sets as arguments.')
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set