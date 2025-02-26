def find_original_set(*sets):
    if len(sets) != 15:
        raise ValueError('Exactly 15 sets must be provided')
    unique_elements = set()
    for s in sets:
        unique_elements.update(s)
    return unique_elements