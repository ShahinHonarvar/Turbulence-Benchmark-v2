def find_original_set(*sets):
    if len(sets) != 15:
        raise ValueError('Function requires exactly 15 distinct sets')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements