def find_original_set(*sets):
    if len(sets) != 8:
        raise ValueError('Function requires exactly 8 distinct sets')
    all_elements = set()
    for s in sets:
        all_elements.update(s)
    return all_elements