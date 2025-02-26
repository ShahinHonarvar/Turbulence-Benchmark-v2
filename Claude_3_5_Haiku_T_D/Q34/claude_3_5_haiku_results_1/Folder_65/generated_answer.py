def find_original_set(*sets):
    if len(sets) != 80:
        raise ValueError('Exactly 80 sets are required')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements