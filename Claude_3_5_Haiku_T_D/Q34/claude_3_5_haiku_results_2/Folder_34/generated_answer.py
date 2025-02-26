def find_original_set(*sets):
    if len(sets) != 95:
        raise ValueError('Function requires exactly 95 sets')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements