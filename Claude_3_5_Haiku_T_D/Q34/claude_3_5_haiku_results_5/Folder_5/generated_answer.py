def find_original_set(*sets):
    if len(sets) != 46:
        raise ValueError('Function requires exactly 46 sets')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements