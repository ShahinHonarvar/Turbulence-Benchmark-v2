def find_original_set(*sets):
    if len(sets) != 43:
        raise ValueError('Function requires exactly 43 sets as arguments')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements