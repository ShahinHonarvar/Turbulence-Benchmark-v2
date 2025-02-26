def find_original_set(*sets):
    if len(sets) != 990:
        raise ValueError('Function requires exactly 990 distinct sets')
    result = set()
    for s in sets:
        result.update(s)
    return result